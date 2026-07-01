"""
mini-agent-loop: 学习用最小 Agent 执行循环。

说明：
- 这是教学用简化实现，不是 LangChain 官方源码。
- 不调用真实 LLM，使用 rule_based_policy 模拟模型/策略决策。
- 目标是理解 Agent loop：plan -> act -> observe -> update -> stop。
"""

from dataclasses import dataclass, field
from typing import Callable, Dict, List, Any


Tool = Callable[[str], str]


@dataclass
class AgentState:
    task: str
    steps: List[Dict[str, Any]] = field(default_factory=list)
    final_answer: str = ""


def search_tool(query: str) -> str:
    """模拟搜索工具。"""
    return f"搜索结果：关于 `{query}` 的资料包括 Agent loop、工具调用、状态管理。"


def calculator_tool(expression: str) -> str:
    """模拟安全计算工具：这里只处理极简加法示例。"""
    if "+" not in expression:
        return "当前 mini 工具只支持形如 1+2 的加法。"
    try:
        left, right = expression.split("+", 1)
        return str(float(left.strip()) + float(right.strip()))
    except ValueError:
        return "计算失败：输入格式不合法。"


def rule_based_policy(state: AgentState) -> Dict[str, str]:
    """
    用规则模拟 LLM 决策。

    返回：
    - action: tool name 或 finish
    - input: 工具输入或最终回答
    """
    task = state.task.lower()

    if not state.steps:
        if "计算" in state.task or "+" in state.task:
            return {"action": "calculator", "input": state.task.replace("计算", "")}
        return {"action": "search", "input": state.task}

    last_observation = state.steps[-1]["observation"]
    return {
        "action": "finish",
        "input": f"基于工具观察，任务 `{state.task}` 的结果是：{last_observation}",
    }


class MiniAgent:
    def __init__(self, tools: Dict[str, Tool], max_steps: int = 3):
        self.tools = tools
        self.max_steps = max_steps

    def run(self, task: str) -> AgentState:
        state = AgentState(task=task)

        for step_id in range(self.max_steps):
            decision = rule_based_policy(state)
            action = decision["action"]
            action_input = decision["input"]

            if action == "finish":
                state.final_answer = action_input
                return state

            if action not in self.tools:
                state.final_answer = f"失败：未知工具 `{action}`。"
                return state

            observation = self.tools[action](action_input)
            state.steps.append(
                {
                    "step": step_id + 1,
                    "action": action,
                    "input": action_input,
                    "observation": observation,
                }
            )

        state.final_answer = "失败：达到最大步数，任务未完成。"
        return state


if __name__ == "__main__":
    agent = MiniAgent(
        tools={
            "search": search_tool,
            "calculator": calculator_tool,
        }
    )

    result = agent.run("帮我解释 Agent loop")
    print("执行轨迹：")
    for step in result.steps:
        print(step)
    print("最终回答：", result.final_answer)
