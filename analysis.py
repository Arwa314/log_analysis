#!/usr/bin/env python3

import psycopg2


def do_query(query):
    # Connect to the news database and execute SQL query
    db = psycopg2.connect(database="news")
    c = db.cursor()
    c.execute(query)
    result = c.fetchall()
    db.close()
    return result


def print_result(result_list, title, ending_word):
    # Printing the result obtaind fron an SQL query
    print("\r\n{}\r\n".format(title))
    for row in result_list:
        for col in row:
            if row.index(col) == 0:
                print("{} ---- ".format(col), end="")
            if row.index(col) == 1:
                print("{} {}.".format(col, ending_word), end="")
        print("\r\n")


# First Query Execution
query1 = """
SELECT articles.title, COUNT(*) AS views
FROM articles, log
WHERE log.path like CONCAT('%', articles.slug )
GROUP BY articles.title
ORDER BY views DESC LIMIT 3;"""
result1 = do_query(query1)

# Second Query Execution
query2 = """
SELECT authors.name, view_count.views
FROM authors, (SELECT articles.author as id, COUNT(*) as views
                FROM articles, log
                WHERE log.path like CONCAT('%', articles.slug )
                GROUP BY articles.author ) AS view_count
WHERE authors.id = view_count.id
ORDER BY view_count.views DESC ;
"""

result2 = do_query(query2)

# Third Query Execution
query3 = """
SELECT day,
       CAST(CAST(error AS FLOAT)/CAST(requests AS FLOAT)*100 AS DECIMAL(10,2))
       AS percent
FROM day_requests
WHERE CAST(CAST(error AS FLOAT)/CAST(requests AS FLOAT)*100 AS DECIMAL(10,2))
      >= 1.0;
"""
result3 = do_query(query3)


if __name__ == '__main__':
    # Printing Results
    print_result(
        result1,
        "The 3 most popular articles are:",
        "Views")

    print_result(
        result2,
        "The authors based on their articles popularity:",
        "Views")

    print_result(
        result3,
        "The days with more than 1% of error requests:",
        "% errors")
