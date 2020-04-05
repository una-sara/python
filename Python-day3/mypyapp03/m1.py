print('m1模块的一个对象创建了...')

#模块内的全局变量就是该模块对象的属性
age = 21 

#模块内的全局函数就是该模块对象的方法
def printAge():
  print('m1:age', age)

def add():
  return  age + 1

#print('m1模块的名称：', __name__)
#print('__name__变量的类型：',  type(__name__))


if(__name__ == '__main__'): #当前模块是启动模块
  #为了检测当前模块正常与否，需要测试——白盒测试
  result = add()
  print('白盒测试结果：', result)