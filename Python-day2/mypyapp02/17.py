#只能在类内部使用的成员——仿private
class Emp:
  def __init__(self, age):
    self.__age = age

  def printAge(self):
    print(self.__age)

#####类的外部###########
e = Emp(30)
#e.__age = -280   #无效的赋值
e.printAge()