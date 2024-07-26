import mysql.connector
mydatabase = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Maralba16!MYSQL",
    database = "staff"
)

mycursor = mydatabase.cursor()

mycursor.execute("SELECT * FROM employees")
for i in mycursor:
    print(i)