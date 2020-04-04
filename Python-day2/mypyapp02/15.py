#面向对象——多态
class Emp :
  def __init__(self, age, ename):
    self.age = age      
    self.ename = ename  
  
  def printInfo(self): 
    print('员工姓名：', self.ename, '员工年龄：', self.age)

#程序员 继承自 员工
class Coder( Emp ):   
  def  __init__(self, age, ename, language):
    super().__init__(age,ename)
    self.language = language

  #子类重写/覆盖父类的同名方法
  def printInfo(self):
    print('员工姓名：', self.ename,'员工年龄：',self.age,'擅长的语言：', self.language)

c3 = Coder(30, 'Scott', 'Java')
c3.printInfo()
c3 = Emp(40,'King')
c3.printInfo()
