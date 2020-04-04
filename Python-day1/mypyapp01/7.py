'''Python中的数组类型'''
#range类型
r2 = range(10)

print(type(r2))
print(r2)  #0/1/2/3/4/5/6/7/8/9

r2 = range(5, 10) 
print(r2)  #5/6/7/8/9

r2 = range(5, 10, 2)   #2表示“步长”
print(r2)   #5/7/9