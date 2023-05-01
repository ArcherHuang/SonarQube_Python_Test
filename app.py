import psycopg2

def get_customer_info(name):
    conn = psycopg2.connect(
        database = "test",
        user = "root",
        password = "qwer1234",
        host = "localhost",
        port = "5432"
    )
    cur = conn.cursor()
    query = "SELECT * FROM users WHERE name = '" + name + "'"
    cur.execute(query)
    rows = cur.fetchall()
    conn.close()
    return rows