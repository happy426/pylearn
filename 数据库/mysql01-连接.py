import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd='huang666'
)

print(mydb)
