'''
 Python中，变量的作用域分为四类：简称LEGB
'''
#list = 30         #全局作用域变量

def outer():
  #list = 20       #嵌入作用域变量
  def inner():
    #list = 10      #局部作用域变量
    print(list)
  return inner

#Python解释器也提供了一个内置函数list--内置作用域

#inner()
f = outer()  
#闭包=公开一个内部函数 + 该函数调用必须的上下文环境
f()
