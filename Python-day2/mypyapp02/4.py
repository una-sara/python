"""
练习：创建一个空数组，用于保存员工姓名；提示“请输入下一位员工姓名(输入end以结束输入：”,程序读取用户输入，保存入空数组；直到用户输入了end，程序输出已经保存的所有员工。  提示：死循环+break
"""
empList = []   #<class list>

while( True ):
  ename = input('请输入下一个员工姓名：')
  if(ename=='end'):
    break
  empList.append( ename )

print('===录入完成===')

"""
i = 0   #列表中元素的下标
while( i<len(empList) ):
  print( empList[i] )
  i += 1
"""

for  e  in  empList :
  print(e)


print('===系统退出===')