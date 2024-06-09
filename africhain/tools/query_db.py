from langchain_community.agent_toolkits import create_sql_agent
from langchain_community.utilities import SQLDatabase
from langchain_core.tools import tool
from langchain_google_genai import ChatGoogleGenerativeAI


@tool
def query_db(question: str) -> str:
    """
    Executes a SQL query against a SQLite database and returns the result as a string.

    Args:
        question (str): The SQL query to execute.

    Returns:
        str: The result of the SQL query.
    """
    db = SQLDatabase.from_uri("sqlite:///data/northwind.db")
    llm = ChatGoogleGenerativeAI(model="gemini-pro", temperature=0.1)

    agent_executor = create_sql_agent(llm, db=db, verbose=True)
    response = agent_executor.invoke(input={"input": question})

    answer = response["output"]
    return answer
