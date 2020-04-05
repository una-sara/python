print('main1启动模块开始运行')

''''
#导入m1模块
#import './m1'   #不需要引号
import  m1     #文件名就是模块名
import  m1     #文件名就是模块名
import  m1     #文件名就是模块名
#import  m2    #模块不存在，ModuleNameError
#print( m1.age )
m1.printAge()
'''

#age = 999

'''
#导入m1模块内部的成员
#import  m1.age  #错误写法
from  m1  import  age
from  m1  import  printAge
print(age)
printAge()
'''
#导入m1模块内部的成员，并取别名
from  m1  import  age  as  m1age
print(m1age)