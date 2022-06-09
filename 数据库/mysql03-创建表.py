import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="huang666",
    database='huang_db'
)

mycursor = mydb.cursor()
# 创建表
# mycursor.execute("create table sites (name varchar(255), id int(255), class varchar(255))")
# 展示表
mycursor.execute("show tables")
for x in mycursor:
    print(x)
# 添加主键 INT AUTO_INCREMENT PRIMARY KEY
mycursor.execute("ALTER TABLE sites ADD COLUMN auto_id INT AUTO_INCREMENT PRIMARY KEY")
# 如果你还未创建 sites 表，可以直接使用以下代码创建。
# mycursor.execute("CREATE TABLE sites (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), url VARCHAR(255))")



