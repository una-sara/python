'''Python中的数组类型'''
#dict类型
myDict = {
    'ename':'Tom',
    'age':20,
    'isMarried':True
}

print(type(myDict))
print(myDict)

print(len(myDict))
#print( myDict[0] )   #NameError
print( myDict['ename'] )
#print( myDict.ename )  #AttributeError
myDict['ename'] = 'Tommy'

#删除元素
del myDict['ename']
#添加元素
myDict['salary'] = 5000
print(myDict)