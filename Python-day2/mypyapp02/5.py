'''
练习：输出九九乘法表
'''
#1.使用while实现  
i = 1
while( i<10 ):
  j = 1
  while( j<=i ):
    print(i, '*', j, '=', i*j, sep="",end=" ")
    j += 1
  print()
  i += 1

print()
#2.使用for实现
for  i  in  range(1, 10):
  for j  in  range(1, i+1):
    print(i,'*',j,'=',i*j, sep="", end=" ")
  print()  
