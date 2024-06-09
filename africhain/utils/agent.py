from langchain import hub
from langchain.agents import AgentExecutor, create_tool_calling_agent
from langchain_core.prompts import ChatPromptTemplate


def build_agent(llm, tools):

    # prompt = ChatPromptTemplate.from_messages(
    #     [
    #         ("system", "you're a helpful assistant"),
    #         ("human", "{input}"),
    #         ("placeholder", "{agent_scratchpad}"),
    #     ]
    # )

    prompt = hub.pull("hwchase17/openai-tools-agent")

    agent = create_tool_calling_agent(llm, tools, prompt)
    return AgentExecutor(agent=agent, tools=tools, verbose=True)
