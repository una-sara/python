'''Python中的数组类型'''
#tuple类型：不可修改的有序数组
myList = [80, 60, 90, 78, 79]

myTuple = tuple( myList )

print( type(myTuple) )
print( myTuple )
print( )

myTuple = ('丁丁', '当当', '豆豆', '丫丫')
print(len(myTuple))  #获取元素个数
print(myTuple[0])
print(myTuple[1:3])

#Tuple中的任何元素都是不可改变的！
#myTuple.append('苗苗')
#myTuple.pop()
#myTuple[0] = '丁当'
#del myTuple[0]

