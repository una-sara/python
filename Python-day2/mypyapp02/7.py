#Python中函数的高阶使用方法

'''
def add(n1, n2):
  sum = n1+n2
  return sum 

#result = add()     #TypeError
#result = add(10)   #TypeError
#result = add(10, 20, 30)   #TypeError
print(result)
'''

#默认值参数
def add(n1, n2=200):
  sum = n1+n2
  return sum 

#result = add()  #TypeError
result = add(10)   #成功执行
result = add(10, 20)   #成功执行
#result = add(10, 20, 30)   #TypeError
print(result)