'''Python中的数组类型'''
#set集合
myList = ['希拉里', '布什', '特没谱', '布什']

print( myList )

#把list强制转换为set
mySet = set( myList )
print(type(mySet))
print(mySet)

#从零开始创建一个set
mySet = {'华盛顿', '克林顿','希拉里','布什' }
print(type(mySet))
print(mySet)


print( len(mySet) )
#print( mySet[0] )  #TypeError 集合元素没有下标

#添加新元素
mySet.add('肯尼迪')
print(mySet)
mySet.add('布什')

#删除元素
mySet.remove('希拉里')
print(mySet)