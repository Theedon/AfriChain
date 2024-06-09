import os

from google.cloud import translate_v2 as translate
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_core.tools import tool

os.environ["TAVILY_API_KEY"] = os.getenv("TAVILY_API_KEY")


@tool
def search_internet(question: str) -> str:
    """do an internet search for the question"""
    search = TavilySearchResults()
    result = search.invoke(question)
    return result
