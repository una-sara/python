#使用第三方模块连接MySQL数据库
import mysql.connector

#连接到指定的MySQL服务器
conn = mysql.connector.connect(
  host='127.0.0.1',
  port='3306',
  user='root',
  password='',
  database='xz'
)
print(type(conn))
print(conn)