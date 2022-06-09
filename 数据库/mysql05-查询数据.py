import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="huang666",
    database='huang_db'
)
mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM sites")
# mycursor.execute("SELECT name, url FROM sites")  # 指定字段，与数据库操作相同。

myresult = mycursor.fetchall()  # fetchall() 获取所有记录
# myresult = mycursor.fetchone()   # fetchone() 获取一条数据
mycursor.close()
for x in myresult:
    print(x)
mydb.close()
