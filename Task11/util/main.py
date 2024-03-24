from db_property_util import DBPropertyUtil
from db_conn_util import DBConnUtil

if __name__ == "__main__":
    

    # Getting database connection using DBConnUtil
    connection = DBConnUtil.get_connection()
    print("Connection Object:", connection)

    # Example: Execute SQL query
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Event")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    # Closing cursor and connection
    cursor.close()
    connection.close()
