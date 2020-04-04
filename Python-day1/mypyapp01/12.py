'''
练习：从键盘读取用户输入的年份数字，输出“该年份是闰年”或者“该年份不是闰年”。提示：闰年计算公式：( ) or ( ()and() )	
'''
year = input('请输入一个年份数字：')
year = int(year)  #把str转换为int

result = (year%400==0) or ((year%4==0)and(year%100!=0))

#result = result ? '是闰年' : '不是闰年'

'''
if(result):
  result = '是闰年'
else :
  result = '不是闰年'
'''
result = '是闰年'  if  result  else  '不是闰年'

print(result)