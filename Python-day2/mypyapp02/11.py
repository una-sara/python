'''
练习：创建函数getLeapYears(start, end)，返回一个数组，其中包含指定范围(start~end)之间所有的闰年
'''
def  getLeapYears(start=2000, end=2100):  #形参指定默认值
  years = []   #list
  for  y  in  range(start, end, 1):
    if((y%400==0)or((y%4==0)and(y%100!=0))):
      years.append(y)
  return years   #务必注意此行的缩进

myList1 = getLeapYears()  #使用形参的默认值
print(myList1)
myList2 = getLeapYears(end=3000, start=2500) #关键字参数
print(myList2)

'''
练习：创建函数getPrimeNumbers(start, end)，返回一个数组，其中包含指定范围(start~end)之间所有的质数
'''
def  getPrimeNumbers(start=2, end=100):
  nums = []
  for n in range(start, end, 1):
    #如果n是质数，则放入nums列表
    i = 2
    while(i<n):
      if(n%i==0):
        break
      i += 1
    ################
    #while退出时有两种可能：①break:n不是闰年  ②i>=n:n是闰年
    if(i>=n):
      nums.append(n)
  return nums

print()
myList3 = getPrimeNumbers()
print(myList3)
myList4 = getPrimeNumbers(100, 150)
print(myList4)