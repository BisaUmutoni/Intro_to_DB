import mysql.connector
from mysql.connector import Error
mydatabase = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Maralba16!MYSQL",
    database = "alx_book_store"
)
def create_database():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Maralba16!MYSQL",
            database = "alx_book_store"
            )

        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")

    except Error as e:
        print(f"Error: {e}")

    finally:
        # Close the cursor and connection
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

if __name__ == "__main__":
    create_database()
