import mysql.connector
import json

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='huang666',
    database='huang_db'
)

mycursor = mydb.cursor()

# table = "create table clsx " \
#         "(id INT AUTO_INCREMENT PRIMARY KEY, car_name varchar(255)," \
#         " direction varchar(255), type8 varchar(255), type17 varchar(255))"
# mycursor.execute(table)

insert = "insert into clsx (car_name, direction,type8,type17) values (%s, %s, %s, %s)"

with open('data/测试集-车辆属性-运输车ms.json', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    for line in lines:
        line_str = json.loads(line)
        name = line_str['url'].split('/')[-1]
        direction = line_str['label'][0]['data'][0]['class'][0]
        type = line_str['label'][0]['data'][0]['class'][1]
        type_car = line_str['label'][0]['data'][0]['class'][-1]
        val = (name, direction, type, type_car)
        mycursor.execute(insert, val)
        mydb.commit()

