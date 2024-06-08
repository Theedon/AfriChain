from langchain_community.utilities import SQLDatabase

from africhain.query_db import query_db, question_to_query

db = SQLDatabase.from_uri("sqlite:///data/northwind.db")


def main():

    question = "how many territories do we have in total"
    query = question_to_query(question, db)
    print(query_db(query, db))


if __name__ == "__main__":
    main()
