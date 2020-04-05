#使用Python系统模块——datetime

#导入模块
#import datetime
#let d = datetime.date()
#let d = datetime.time()
#let d = datetime.datetime()

#导入模块中的成员
#from datetime import date
#from datetime import time
from datetime import datetime

#获取当前系统日期时间：
dt = datetime.now()
print( type(dt) )
print( dt )

#把日期时间格式化为特殊的字符串：
y = dt.year
m = dt.month
d = dt.day    #JS中获取“日”用的是date
h = dt.hour
mi = dt.minute
s = dt.second
print(y, '-', m, '-', d, ' ', h,':',mi,':',s, sep="")
#把日期时间格式化为特殊的字符串：
s = dt.strftime('%Y-%m-%d %H:%M:%S')
print(s)


#把日期时间转换为长整数：
num = dt.timestamp()
print( type(num) )  #<class float>
print( num )  #以秒为单位的浮点数，精确到微秒
#print( int(num*1000) ) #以毫秒为单位的整数

#把长整数转换为日期时间对象：
num = 0
num = 60   #整数位表示秒钟
num = 3600
dt = datetime.fromtimestamp(num)
print(dt)
