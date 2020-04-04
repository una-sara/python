#Python中函数的高阶使用方法

#可变数量的参数——如何实现任意多个数字的相加？
def add( *nums ):
  #print(type(nums))    #<class 'tuple'>
  #print(nums)
  sum = 0
  for  n  in  nums:
    sum += n
  return sum

#调用有可变数量参数的函数
result = add()               #实参是()
result = add(10)             #实参是(10,)
result = add(10,20)          #实参是(10,20)
result = add(10,20,30,40)    #实参是(10,20,30,40)
print(result)