from langchain_community.utilities import SQLDatabase

from africhain.query_db import query_db

db = SQLDatabase.from_uri("sqlite:///data/northwind.db")


def main():

    question = "list the employee names for me descending order"
    result = query_db(question, db)
    print(result)


if __name__ == "__main__":
    main()
