from langchain import hub
from langchain.agents import AgentExecutor, create_tool_calling_agent


def build_agent(llm, tools):

    prompt = hub.pull("hwchase17/openai-tools-agent")

    agent = create_tool_calling_agent(llm, tools, prompt)
    return AgentExecutor(agent=agent, tools=tools, verbose=True)
