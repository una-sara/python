#使用Python系统模块——random

import random as r

#生成0~1间的随机小数：
n = r.random() 
print( n )
n = r.random() 
print( n )
n = r.random() 
print( n )
  
#生成min~max间的随机整数，例1000~10000：
#JS:  parseInt(Math.random()*(10000-1000)+1000)
n = r.randrange(1000, 10000, 1)
print( n )
n = r.randrange(1000, 10000)
print( n )
n = r.randrange(1000, 10000, 100)
print( n )
  
#从字符串数组中随机取出一个元素：
empList = ['亮亮','然然','东东','涛涛']
#JS只能：0~4产生随机整数， empList[n]
e = r.choice( empList )
print( e )
  
#随机打乱一个数组：
r.shuffle(empList)
print(empList)