# jarvis-base
LLM Agent base

1. 基于 LLM 的智能代理
2. 针对细分场景的专业知识库增强
3. 自动决策工具调度使用
4. 可持久化的记忆系统
5. 情绪判断与对应反馈
6. API 与系统集成
7. 智能语音合成
8. LLM 工程化

## 技术架构分析

1. 资源层

    Redis / LLM / Config / VectorStore / API

2. 服务层

    FastAPI / LangChain(Prompt, Agent)

3. API 层

    API / LangSmith(LLM 层监控)

4. APP

    Telegram bot / 数智人