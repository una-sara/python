#Python中的函数高阶应用

def  connect( host, user, pwd, port, dbname ):
  print('正在连接主机：', host)
  print('服务器端口号：', port)
  print('服务器用户名：', user)
  print('服务器密码名：', pwd)
  print('数据库的名称：', dbname)

#调用函数——如果参数过多，往往不容易记住参数的顺序
#connect('127.0.0.1', 3306, 'xuezi', 'root', '123456')
#解决方案1： def  connect( options ): 
#解决方案2： 使用关键字参数
connect(port=3306, dbname='xuezi', user='root', pwd='123456', host='127.0.0.1')