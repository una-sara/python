#面向对象——封装
class Emp :
  def __init__(self, age, ename):
    print('一个Emp对象被构建了')
    self.age = age      #在对象中封装属性
    self.ename = ename  #在对象中封装属性
  
  def printInfo(self):  #在对象中封装方法
    print(self.age,  self.ename)

#创建类的实例——创建对象
e1 = Emp(25, 'King')
#print(e1.age, e1.ename)
e1.printInfo()

e2 = Emp(22, 'Jerry')
#print(e2.age, e2.ename)
e2.printInfo()