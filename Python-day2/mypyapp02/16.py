'''
练习：画图板应用中需要一个类Shape，有属性fillColor、borderColor，以及两个方法getSize()、getPerimeter()；继续创建类Circle和Rectangle，都继承自Shape，但是分别多了属性：半径(r)、宽(with)和高(height)，试着创建这三个类
'''
#分析：Circle is a Shape、 Rectangle is a Shape
class Shape :
  def __init__(self, fillColor, borderColor):
    self.fillColor = fillColor
    self.borderColor = borderColor
    print('一个Shape对象被构建了')
  def getSize(self):
    return 0
  def getPerimeter(self):
    return 0
####################################
class Circle(Shape):
  def __init__(self, fillColor, borderColor, r):
    super().__init__(fillColor, borderColor) 
    self.r = r
    print('一个Circle对象被构建了')  
  def getSize(self):
    return 3.14 * self.r * self.r
  def getPerimeter(self):
    return 2 * 3.14 * self.r
####################################
class Rectangle(Shape):
  def __init__(self, fillColor, borderColor, width, height):
    super().__init__(fillColor, borderColor) 
    self.width = width
    self.height = height
    print('一个Rectangle对象被构建了')  
  def getSize(self):
    return self.width * self.height
  def getPerimeter(self):
    return 2 * (self.width + self.height)

s1 = Shape('填充红', '边框黄')
print( s1.getSize() )
print( s1.getPerimeter() )

s1 = Circle('填充红', '边框黄', 10)
print( s1.getSize() )
print( s1.getPerimeter() )

s1 = Rectangle('填充红', '边框黄', 20, 30)
print( s1.getSize() )
print( s1.getPerimeter() )