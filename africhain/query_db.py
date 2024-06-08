from langchain.chains import create_sql_query_chain
from langchain_community.utilities import SQLDatabase
from langchain_huggingface import HuggingFaceEndpoint

db = SQLDatabase.from_uri("sqlite:///data/northwind.db")


def query_db(query):
    print(db)
    print(db.dialect)
    print(db.get_usable_table_names)

    result = db.run(query)
    print(result)
    return result


def question_to_query(question: str):
    llm = HuggingFaceEndpoint(
        repo_id="HuggingFaceH4/zephyr-7b-beta",
        model_kwargs={"temperature": 0.5, "max_length": 64, "max_new_tokens": 512},
    )

    chain = create_sql_query_chain(llm, db)
    response = chain.invoke({"question": "How many customers are there"})
    # print(response)

    return response
