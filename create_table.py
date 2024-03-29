import psycopg2
from sql_queries import create_table_queries, drop_table_queries 

def create_database():
    """
    Establish database connection and return's the connection and cursor references.
    :return: return's (cur, conn) a cursor and connection reference
    """
    # connect to the default database 
    conn = psycopg2.connect(host="localhost",
    dbname="postgres",
    user="postgres",
    password="10121998",)
    conn.set_session(autocommit=True)
    cur = conn.cursor()

    # create sparkify database with UTF8 encoding
    cur.execute("DROP DATABASE IF EXISTS sparkifydb")
    cur.execute("CREATE DATABASE sparkifydb WITH ENCODING 'utf8' TEMPLATE template0")

    # close the connection to the database 

    conn = psycopg2.connect(host="localhost",
    dbname="sparkifydb",
    user="postgres",
    password="10121998",)
    cur = conn.cursor()

    return cur, conn

def drop_table(cur, conn):
    """
    Run's all the drop table queries defined in the sql_queries.py
    :param cur: cursor to the database
    :param conn: database connection reference
    """
    for query in drop_table_queries:
        cur.execute(query)
        conn.commit()

def create_tables(cur,conn):
    """
    Run's all the create table queries defined in sql_queries.py
    :param cur: cursor to the database
    :param conn: database connection reference
    """
    for query in create_table_queries:
        cur.execute(query)
        conn.commit()

def main():
    """
    Driver main function
    """
    cur, conn = create_database()

    drop_table(cur,conn)
    print("Table dropped successfully!!")

    create_tables(cur,conn)
    print("Table created successfully!!")

    conn.close()

if __name__ == "__main__":
    main()