#if..elif..else的使用

#购物总价满500打八折
#sum = 450
sum = 600

'''
if(sum>=500):
      print('语句1')
      print('语句2')
print('语句3')
'''

if(sum>=500):
  sum *= 0.8
  print('符合满500打八折条件')

print('应付总价:', sum)

