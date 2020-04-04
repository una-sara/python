'''Python中的数组类型'''
#list类型：可修改的有序数组
myList = [80, 60, 90, 78, 79]

print(type(myList))
print(myList[0])  #获取指定下标处元素
print(myList[-1]) #获取结尾处元素
print(myList[1:4]) #获取指定范围内的子列表
print(myList[1:])  #获取指定开始直到结尾的子列表
print(len(myList))  #获取列表中的元素个数

print(myList)
#添加新元素
#myList.push(50)  #AttributeError，没有push方法
myList.append(50) #在列表尾部追加新元素
#删除已有元素
myList.pop()      #在列表尾部删除元素
#删除指定下标处的元素     myList.remove(0)
del  myList[0]

print(myList) 