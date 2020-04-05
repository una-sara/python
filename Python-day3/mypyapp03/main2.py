print('main2启动模块开始运行')

'''
#导入包下模块
import user.login
import user.login
import user.login
print('login:', user.login.uname)
print('login:', user.login.upwd)
'''
#导入包下模块
import user.login  as  ul
print('login:', ul.uname)
print('login:', ul.upwd)

#导入包下模块
import user.register  as  ur
print('register:', ur.uname)
print('register:', ur.upwd)