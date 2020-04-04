#面向对象——继承
#理论上：继承的本质是 IS A 的关系
#例如：Coder is a Emp、  Circle is a Shape、 Boss is a Enemy
class Emp :
  def __init__(self, age, ename):
    print('一个Emp对象被构建了')
    self.age = age      
    self.ename = ename  
  
  def printInfo(self): 
    print('员工姓名：', self.ename, '员工年龄：', self.age)

#程序员 继承自 员工
class Coder( Emp ):   #Python中使用()表示继承
  def  __init__(self, age, ename, language):
    #在子类体内构建一个父类对象，再调用其构造方法
    super().__init__(age,ename)
    self.language = language


c3 = Coder(30, 'Scott', 'Java')
#print(c3.age)
#print(c3.ename)
#print(c3.language)
c3.printInfo()
