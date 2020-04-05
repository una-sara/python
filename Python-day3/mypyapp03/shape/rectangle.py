print('rectangle模块实例被创建了')

w = 20
h = 10

def getSize():
  return w * h

def getPerimeter():
  return 2 * (w + h)

#单元测试——只在当前模块作为启动模块时执行
if(__name__ == '__main__'):
  print('====rectangle模块测试====')
  print( getSize() )
  print( getPerimeter() )