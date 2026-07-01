# 三、LlamaIndex / RAG 高频面试题

## Q14：LlamaIndex 的核心定位是什么？

**候选人回答：** LlamaIndex 的核心是 context augmentation：把企业私有数据通过连接器、解析、索引、检索和查询引擎提供给 LLM。它非常适合知识库问答、文档理解、信息抽取和 Data Agent。

**追问：** 它和 LangChain 的区别？答：LlamaIndex 更偏数据/RAG/索引/检索；LangChain 更偏通用 Agent 应用集成；复杂系统中二者可以组合。

## Q15：一个完整 RAG pipeline 包含哪些步骤？

**候选人回答：** 数据接入 → 清洗/解析 → chunking → embedding → 建索引 → query rewrite → retrieval → rerank → context packing → generation → citation → evaluation。面试中最忌只说“向量数据库 + 大模型”。

**追问：** RAG 出错通常错在哪里？答：数据源质量、切块、embedding、召回、rerank、上下文拼接、Prompt 约束、模型生成和引用校验都可能出错。

## Q16：Chunking 怎么设计？

**候选人回答：** 按语义边界切分优于固定长度硬切。需要考虑文档结构、标题层级、表格、代码块、公式、重叠窗口、chunk size 和 metadata。长 chunk 上下文完整但召回不精确；短 chunk 精确但可能丢语义。

**追问：** 如何处理 PDF 表格和图片？答：用更强的 parser/OCR，把表格转结构化文本或 markdown，图片可用 multimodal parser/vision model 提取说明，并保留页码、标题、图表编号等 metadata。

## Q17：向量检索、关键词检索和混合检索怎么选？

**候选人回答：** 向量检索擅长语义相似；BM25/关键词擅长精确术语、编号、专有名词；混合检索适合企业知识库，因为用户问题既有自然语言表达，也有产品名、错误码、合同条款等精确匹配需求。

**追问：** 召回太多噪声怎么办？答：metadata filter、reranker、query decomposition、score threshold、去重、上下文压缩。

## Q18：Reranker 的作用是什么？

**候选人回答：** Retriever 负责从大库里快速召回候选，reranker 负责对候选与 query 的相关性重新排序。它通常更慢但更准，适合 top-k 候选后处理。

**追问：** 什么时候不用 reranker？答：低延迟、低成本、语料简单、召回已经足够精准时可以不用；生产中可按问题复杂度动态启用。

## Q19：如何减少 RAG 幻觉？

**候选人回答：** 从三层控制：检索层提高召回和相关性；生成层强制基于证据回答并给引用；系统层在证据不足时拒答或转人工。还要做 faithful evaluation，检查答案是否被上下文支持。

**追问：** 模型回答了知识库没有的内容怎么办？答：加入“无证据不回答”规则、引用校验、答案-证据一致性检测和低置信度降级。

## Q20：LlamaIndex Agent 如何使用 RAG？

**候选人回答：** 在 LlamaIndex 中，RAG pipeline 可以作为 Agent 的一个工具。Agent 不只是回答问题，还可以根据任务选择查知识库、查数据库、调用 API、做抽取或生成报告。

**追问：** 何时用 Query Engine，何时用 Agent？答：固定问答用 Query Engine；需要多步决策、工具选择和跨数据源操作时用 Agent。
