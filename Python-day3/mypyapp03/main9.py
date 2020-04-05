#使用Python系统模块——json
import  json
from datetime import datetime

#把对象转换为JSON字符串——序列化
#dict
obj = {
  'uname':'丁当', 
  'age':20, 
  'isMarried':True, 
  #'birthday':datetime.now()  #Pyhton中datetime不能序列化
}
s = json.dumps(obj)   #JSON.stringify()
print( type(s) )
print( s )

#把字符串解析为对象——反序列化  #JSON.parse()
obj = json.loads( s )
print(type(obj))
print(obj)


