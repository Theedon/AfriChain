import os

from langchain.chains import create_sql_query_chain
from langchain_google_genai import ChatGoogleGenerativeAI

from africhain.utils.replace_md import unmark

google_api_key = os.getenv("GOOGLE_API_KEY")


def query_db(query, db):
    # print(db.dialect)
    # print(db.get_usable_table_names)

    result = db.run(query)
    return result


def question_to_query(question: str, db):
    llm = ChatGoogleGenerativeAI(
        model="gemini-pro", temperature=0.1, google_api_key=google_api_key
    )
    chain = create_sql_query_chain(llm, db)
    response = chain.invoke({"question": f"{question}"})
    clean_response = unmark(response)

    return clean_response
