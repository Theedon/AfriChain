import os

from langchain.chains import create_sql_query_chain
from langchain_community.utilities import SQLDatabase
from langchain_google_genai import ChatGoogleGenerativeAI

from africhain.utils.replace_md import unmark

db = SQLDatabase.from_uri("sqlite:///data/northwind.db")


def query_db(query, db=db):
    print(db)
    print(db.dialect)
    print(db.get_usable_table_names)

    result = db.run(query)
    print(result)
    return result


google_api_key = os.getenv("GOOGLE_API_KEY")


def question_to_query(question: str, db=db):
    llm = ChatGoogleGenerativeAI(
        model="gemini-pro", temperature=0.1, google_api_key=google_api_key
    )
    chain = create_sql_query_chain(llm, db)
    response = chain.invoke({"question": "How many customers are there"})
    clean_response = unmark(response)


    print(db.run(clean_response))
    # print(response)

    return clean_response
