import os

from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_core.tools import tool

os.environ["TAVILY_API_KEY"] = os.getenv("TAVILY_API_KEY")


@tool
def search_internet(question: str) -> str:
    """
    Performs a search on the internet using the Tavily search engine and returns the results.

    Args:
        question (str): The search query to be executed.

    Returns:
        str: The search results from the Tavily search engine.
    """
    search = TavilySearchResults()
    result = search.invoke(question)
    return result
