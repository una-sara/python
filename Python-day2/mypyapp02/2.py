'''
练习:创建变量表示用户的积分,如果达到了10000分,输出"黑金用户";  否则如果达到了5000分,输出"黄金用户";  否则如果达到1000分,输出"白银用户";  否则输出"普通用户"
'''

#score = 30000
#score = 8000
#score = 2000
score = 200

if(score>=10000):
  print('黑金用户')
elif(score>=5000):
  print('黄金用户')
elif(score>=1000):
  print('白银用户')
else:
  print('普通用户')

print('程序运行结束')