import os

from langchain import hub
from langchain.agents import AgentExecutor, create_tool_calling_agent
from langchain_anthropic import ChatAnthropic
from langchain_community.utilities import SQLDatabase
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.pydantic_v1 import BaseModel, Field
from langchain_core.tools import tool
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_mistralai.chat_models import ChatMistralAI
from langchain_openai import ChatOpenAI

from africhain.utils.get_ip_info import get_ip_info
from africhain.utils.get_weather import get_weather
from africhain.utils.search_internet import search_internet

# from africhain.query_db import query_db

os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")
os.environ["HUGGINGFACEHUB_API_TOKEN"] = os.getenv("HUGGINGFACEHUB_API_TOKEN")
os.environ["HF_TOKEN"] = os.getenv("HF_TOKEN")
os.environ["MISTRAL_API_KEY"] = os.getenv("MISTRAL_API_KEY")
os.environ["TOGETHER_API_KEY"] = os.getenv("TOGETHER_API_KEY")
os.environ["ANTHROPIC_API_KEY"] = os.getenv("ANTHROPIC_API_KEY")


def main():
    # llm = ChatOpenAI(model="gpt-3.5-turbo-0125")
    # llm = ChatGoogleGenerativeAI(model="gemini-pro", temperature=0.1)
    # llm = ChatMistralAI(model="mistral-large-latest")

    # llm = ChatOpenAI(
    #     base_url="https://api.together.xyz/v1",
    #     api_key=os.environ["TOGETHER_API_KEY"],
    #     model="mistralai/Mixtral-8x7B-Instruct-v0.1",
    # )

    llm = ChatAnthropic(model="claude-3-sonnet-20240229")

    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", "you're a helpful assistant"),
            ("human", "{input}"),
            ("placeholder", "{agent_scratchpad}"),
        ]
    )

    prompt = hub.pull("hwchase17/openai-tools-agent")

    tools = [search_internet, get_weather, get_ip_info]

    agent = create_tool_calling_agent(llm, tools, prompt)
    agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)
    agent_executor.invoke(
        {"input": "what are the information of the ip address 102.88.68.222"},
    )


if __name__ == "__main__":
    main()
