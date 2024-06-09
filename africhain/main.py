import os

from langchain import hub
from langchain.agents import AgentExecutor, create_tool_calling_agent
from langchain_anthropic import ChatAnthropic
from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_mistralai.chat_models import ChatMistralAI
from langchain_openai import ChatOpenAI

from africhain.tools.ip import get_ip_info
from africhain.tools.movie import get_movie_info
from africhain.tools.pokemon import get_pokemon_info
from africhain.tools.query_db import query_db
from africhain.tools.weather import get_weather
from africhain.tools.web_search import search_internet
from africhain.utils.agent import build_agent

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

    tools = [
        query_db,
        search_internet,
        get_weather,
        get_ip_info,
        get_pokemon_info,
        get_movie_info,
    ]

    agent_executor = build_agent(llm, tools)
    result = agent_executor.invoke(
        {"input": "how many employees are in the database"},
    )
    print(result["output"])


if __name__ == "__main__":
    main()
