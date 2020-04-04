#Python中函数的高阶使用方法

#可变数量的参数——如何实现任意多个数字的相加？
#计算一年的总收入：
def getTotalSalary( **money ):
  print(type(money))
  print(money)

#调用函数
getTotalSalary(jan=1000, feb=3000, may=5000)
  