from africhain.query_db import query_db, question_to_query


def main():
    # print("hello wworld")
    query = "SELECT CustomerID FROM Customers LIMIT 10;"
    # query_db(query)

    question = {"question": "How many customers are there"}
    print(question_to_query(question))


if __name__ == "__main__":
    main()
