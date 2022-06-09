## 使用框架
1. 连接数据库connect
2. 创建游标cursor
3. 执行SQL语句execute
4. (获取执行结果 fetchall)
5. 关闭游标
6. (提交执行结果 commit)
7. 关闭数据库连接


## 下载mysql连接驱动
pip install  mysql-connector-python -i https://pypi.tuna.tsinghua.edu.cn/simple

## 创建数据库
创建一个名为<font color=DeepSkyBlue>huang_db</font>的数据库（mysql02.py）

## 创建表
```
mycursor.execute("create table sites (name varchar(255), id int(255), class varchar(255))")
```
### 添加主键 
INT AUTO_INCREMENT PRIMARY KEY

```
mycursor.execute("ALTER TABLE sites ADD COLUMN auto_id INT AUTO_INCREMENT PRIMARY KEY")
```
## 增删改查操作
### <font color=DeepSkyBlue>注意！！！</font>
UPDATE 语句要确保指定了 WHERE 条件语句，否则会导致整表数据被更新。
为了防止数据库查询发生 SQL 注入的攻击，我们可以使用 %s 占位符来转义更新语句的条件：
### 增
```
insert into sites (name, id, class) values (%s, %s, %s)
val = ("huang", 1857117, "信计一班")
mycursor.execute(sql, val)
mydb.commit()  # 数据表内容有更新，必须使用到该语句
```
### 删
删除表使用 "DROP TABLE" 语句， IF EXISTS 关键字是用于判断表是否存在，只有在存在的情况才删除：

```
sql = "DROP TABLE IF EXISTS sites"  # 删除数据表 sites

DELETE FROM sites WHERE name = 'stackoverflow'
```

### 改
```
UPDATE sites SET name = 'ZH' WHERE name = 'Zhihu'
```
### 查
select 语句


