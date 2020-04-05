print('main4启动模块开始运行')

'''
#导入包中的模块
import shape.circle  as  c
import shape.rectangle  as  r

print('圆形的面积：',  c.getSize() )
print('圆形的周长：',  c.getPerimeter() )

print('矩形的面积：',  r.getSize() )
print('矩形的周长：',  r.getPerimeter() )
'''

#导入包中的模块下的成员
from  shape.circle  import getSize as circleSize, getPerimeter as circlePerimeter

from  shape.rectangle  import getSize as rectSize, getPerimeter as rectPerimeter

print('圆形的面积：', circleSize())
print('圆形的周长：', circlePerimeter())
print('矩形的面积：', rectSize())
print('矩形的周长：', rectPerimeter())