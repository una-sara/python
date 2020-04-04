#字符串的使用
msg = '''hello world'''
#msg = '大内科技集团有限公司'

#获取字符串的长度
#print( msg.length )  错误写法！
print( len(msg) )

print( msg[0] )  #获取指定下标处的字符
print( msg[len(msg)-1] )  #获取结尾的字符
print( msg[-1] )  #获取结尾的字符
print( msg[1:3] )  #获取指定范围内的字符
print( msg[1:] )  #获取指定指定起始处直到结尾的字符

print( msg.upper() )      #转换为纯大写
print( msg.lower() )      #转换为纯小写
print( msg.capitalize() ) #第一个首字母大写
print( msg.title() )      #每个单词第一个首字母大写