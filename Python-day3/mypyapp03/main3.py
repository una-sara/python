print('main3启动模块开始运行')

#导入包下的模块中的成员
#import user.login.uname   #错误
#print(user.login.uname)
from user.login import uname, upwd
print('login:', uname)
print('login:', upwd)

from user.register  import uname as rUname, upwd as rUpwd
print('register:', rUname)
print('register:', rUpwd)