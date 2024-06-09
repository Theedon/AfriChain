import os

from langchain_community.agent_toolkits import create_sql_agent
from langchain_google_genai import ChatGoogleGenerativeAI

# from langchain_huggingface import HuggingFaceEndpoint

os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")
os.environ["HUGGINGFACEHUB_API_TOKEN"] = os.getenv("HUGGINGFACEHUB_API_TOKEN")
os.environ["HF_TOKEN"] = os.getenv("HF_TOKEN")


def query_db(question: str, db):
    # llm = HuggingFaceEndpoint(
    #     max_new_tokens=512,
    #     repo_id="google/gemma-7b",
    #     temperature=0.7,
    # )

    llm = ChatGoogleGenerativeAI(
        model="gemini-pro",
        temperature=0.1,
    )

    agent_executor = create_sql_agent(llm, db=db, verbose=True)
    response = agent_executor.invoke(input={"input": question})

    answer = response["output"]
    return answer
