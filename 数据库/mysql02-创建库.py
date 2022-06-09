import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="huang666"
)

mycursor = mydb.cursor()
# 创建数据库
# mycursor.execute("CREATE DATABASE huang_db")
mycursor.execute("show databases")
for x in mycursor:
    print(x)
print(mycursor)


# 直接连数据库
# import mysql.connector
#
# mydb = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     passwd="huang666",
#     database="huang_db"
# )


