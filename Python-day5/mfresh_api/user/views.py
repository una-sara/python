from django.http import JsonResponse
from .models import MfUser

'''
1.1 用户登录验证
API地址：	/user/login
处理方法：	userLogin( req )
请求方法：	GET
请求参数：	查询字符串：
unameOrPhone-用户名或电话号码，必需
upwd-密码，必需
响应结果：	{"code":1,"uid":1,"uname":"test","phone":"13012345678"}
或
{"code":400}
'''
def  userLogin(req):
  #读取请求数据
  np = req.GET.get('unameOrPhone')
  p = req.GET.get('upwd')
  #执行数据库登录验证
  #SELECT * FROM mf_user WHERE (()AND()) OR (()AND())
  result = MfUser.objects.filter(uname=np, upwd=p) | MfUser.objects.filter(phone=np, upwd=p)
  if(len(result)>0):
    u = result[0]  #查询到的用户
    data = {'code':1, 'uid':u.uid, 'uname':u.uname, 'phone':u.phone}
  else :
    data = {'code':400}
  #输出响应消息
  res = JsonResponse( data )
  res['Access-Control-Allow-Origin'] = '*'
  return res

'''
1.2 注册新用户
API地址：	/user/register
处理方法：	userRegister( req )
请求方法：	POST
请求参数：	请求主体(application/x-www-form-urlencoded)：
  uname-用户名，必需
  upwd-密码，必需
  phone-电话号码，必需
响应结果：	{"code":1,"uid":3,"uname":"test"}
或
{"code":500}
'''
def  userRegister(req):
  #读取请求数据
  n = req.POST.get('uname')   #请求主体数据：用户名
  p = req.POST.get('upwd')    #请求主体数据：密码
  h = req.POST.get('phone')   #请求主体数据：手机号
  #执行数据库插入操作
  u = MfUser.objects.create(uname=n, upwd=p, phone=h)
  if(u):
    data = {'code':200,'uid':u.uid, 'uname':u.uname}
  else:
    data = {'code':500}
  #输出响应消息
  res = JsonResponse( data )  #dict会被自动序列化
  res['Access-Control-Allow-Origin'] = '*'
  return res

'''
1.3 验证用户名是否已经存在
API地址：	/user/check/uname
处理方法：	userCheckUname( req )
请求方法：	GET
请求参数：	查询字符串：
  uname-用户名，必需
响应结果：	{"code":1,"msg":"exist"}  存在
或
{"code":2,"msg":"non-exist"}  不存在
'''
def  userCheckUname(req):
  #读取请求数据
  n = req.GET.get('uname')
  #执行数据库查询，看看插件结果的数量select * from..where
  result = MfUser.objects.filter(uname=n).values()
  if(len(result)>0):
    data = {'code':1, 'msg':'exist'}
  else:
    data = {'code':2, 'msg':'non-exist'}
  #输出响应消息
  res = JsonResponse(data)
  res['Access-Control-Allow-Origin'] = '*'
  return res

'''
1.4 验证电话号码是否已经存在
API地址：	/user/check/phone
处理方法：	userCheckPhone( req )
请求方法：	GET
请求参数：	查询字符串：
  phone-用户名，必需
响应结果：	{"code":1,"msg":"exist"}  存在
或
{"code":2,"msg":"non-exist"}  不存在
'''
def  userCheckPhone(req):
  #读取请求数据
  p = req.GET.get('phone')
  #执行数据库验证
  result = MfUser.objects.filter(phone=p).values()
  if(len(result)>0):
    data = {'code':1, 'msg':'exist'}
  else:
    data = {'code':2, 'msg':'non-exist'}
  #输出响应消息
  res = JsonResponse(data)
  res['Access-Control-Allow-Origin'] = '*'
  return res