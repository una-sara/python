#类内部的静态成员——仿static效果
class Emp:
  location = '中国'   #类属性——整个类中只有一份
  
  def __init__(self, age):
    self.age = age    #实例属性——每个对象内都有一份


e1 = Emp(20)
e2 = Emp(30)
print(e1.age)
print(e2.age)
e2.age = 50
print(e1.age)
print(e2.age)

print(Emp.location)
print(e1.location)
print(e2.location)
Emp.location = '美国'

print()
print(Emp.location)
print(e1.location)
print(e2.location)