"""
mini-langgraph: 学习用最小状态图执行器。

说明：
- 这是教学用简化实现，不是 LangGraph 官方源码。
- 目标是理解 StateGraph / Node / Edge / Conditional Edge / Checkpoint 的基本思想。
"""

import json
from pathlib import Path
from typing import Any, Callable, Dict, Optional


State = Dict[str, Any]
NodeFn = Callable[[State], State]
RouteFn = Callable[[State], str]

START = "__start__"
END = "__end__"


class StateGraph:
    def __init__(self):
        self.nodes: Dict[str, NodeFn] = {}
        self.edges: Dict[str, str] = {}
        self.conditional_edges: Dict[str, RouteFn] = {}

    def add_node(self, name: str, fn: NodeFn) -> None:
        self.nodes[name] = fn

    def add_edge(self, source: str, target: str) -> None:
        self.edges[source] = target

    def add_conditional_edges(self, source: str, router: RouteFn) -> None:
        self.conditional_edges[source] = router

    def invoke(self, state: State, checkpoint_path: Optional[str] = None) -> State:
        current = self.edges.get(START)
        if current is None:
            raise ValueError("Graph must define an edge from START.")

        while current != END:
            if current not in self.nodes:
                raise ValueError(f"Unknown node: {current}")

            state = self.nodes[current](state)
            state.setdefault("trace", []).append(current)

            if checkpoint_path:
                self._save_checkpoint(state, checkpoint_path)

            if current in self.conditional_edges:
                current = self.conditional_edges[current](state)
            else:
                current = self.edges.get(current, END)

        return state

    @staticmethod
    def _save_checkpoint(state: State, checkpoint_path: str) -> None:
        path = Path(checkpoint_path)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(state, ensure_ascii=False, indent=2), encoding="utf-8")


def classify_intent(state: State) -> State:
    user_input = state["user_input"]
    if "退款" in user_input:
        state["intent"] = "refund"
    else:
        state["intent"] = "qa"
    return state


def answer_question(state: State) -> State:
    state["answer"] = "这是一个普通问答请求，系统直接回答。"
    return state


def request_human_approval(state: State) -> State:
    state["need_human_approval"] = True
    state["answer"] = "退款属于高风险动作，需要人工审批后执行。"
    return state


def route_by_intent(state: State) -> str:
    if state.get("intent") == "refund":
        return "human_approval"
    return "qa_answer"


if __name__ == "__main__":
    graph = StateGraph()
    graph.add_node("classify", classify_intent)
    graph.add_node("qa_answer", answer_question)
    graph.add_node("human_approval", request_human_approval)

    graph.add_edge(START, "classify")
    graph.add_conditional_edges("classify", route_by_intent)
    graph.add_edge("qa_answer", END)
    graph.add_edge("human_approval", END)

    result = graph.invoke(
        {"user_input": "我想申请退款", "trace": []},
        checkpoint_path="checkpoints/latest.json",
    )
    print(result)
