#Python中的函数
'''
#声明函数
def add():
  n1 = 10
  n2 = 20
  sum = n1+n2
  print( sum )

#调用函数
add()
'''

"""
#声明函数
def add(n1, n2):
  sum = n1+n2
  print( sum )

#调用函数
add(10, 20)
add(100, 200)
"""

#声明函数
def add(n1, n2):
  sum = n1+n2
  return sum 

#调用函数
result = add(1.5, 2.5)
print(result)