import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="huang666",
    database='huang_db'
)

mycursor = mydb.cursor()
sql = "insert into sites (name, id, class) values (%s, %s, %s)"

# # 单行插入
# val = ("huang", 1857117, "信计一班")
# mycursor.execute(sql, val)
# mydb.commit()  # 数据表内容有更新，必须使用到该语句
# print(mycursor.rowcount, "success")

# 多条插入
val = [
    ("杰哥", 1857125, "信计一班"),
    ("帆帆", 1857123, "信计一班"),
    ("舒心", 1857109, "信计一班"),
    ("盛源", 1851100, "计科一班")
]
mycursor.executemany(sql, val)
mydb.commit()
print(mycursor.rowcount, 'rows succeed!!!')

