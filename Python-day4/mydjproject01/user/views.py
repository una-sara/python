from django.http import HttpResponse

#路由方法：处理客户端发起的用户登录请求
def userLogin( req ):
  #假设：客户端提交了?uname=dang&upwd=123
  #print( req.GET )  #QueryDict
  #print( req.GET['uname'] )  #若客户端未提交则抛出错误
  print( req.GET.get('uname','guest') )
  res = HttpResponse('<h3>USER LOGIN</h3>')
  return res

#路由方法：处理客户端发起的用户注册请求
def userRegister( req ):
  res = HttpResponse('<h3>USER REGISTER</h3>')
  return res