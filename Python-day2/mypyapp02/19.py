'''
示例：请用户从键盘输入两个数字，程序计算出数字的商，输出在屏幕上
'''
try:
  n1 = input('请输入被除数：')
  n1 = int(n1)  #解析字符串得到整数,可能发生ValueError
  if(n1<0):
    raise Exception('被除数不能小于0') #手工抛出自定义错误
  n2 = input('请输入除数：')
  n2 = int(n2)  #解析字符串得到整数,可能发生ValueError
  n3 = n1 / n2  #执行算术除法,可能发生ZeroDivisionError
  print('两个数的商为:', n3)
except ValueError as e:         #专门捕捉值错误异常
  print('您输入的数字格式非法')
  print(e)
except ZeroDivisionError as e:  #专门捕捉被0除异常
  print('除数不能为0')
  print(e)
except Exception as e:          #捕捉所有异常
  print('发生了运行异常')
  print(e)
finally:              #无论异常发生与否都要执行的
  print('===程序运行结束===')