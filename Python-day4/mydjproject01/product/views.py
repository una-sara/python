from django.http import HttpResponse
from django.http import JsonResponse

#路由方法：处理客户端的“商品列表”请求
def  productList( req ):
  '''
  #向客户数返回HTML响应
  res = HttpResponse('<h3>商品列表</h3><hr>')
  res['Access-Control-Allow-Origin'] = '*'
  res['Server'] = 'TEDU WebServer'
  return res
  '''
  #向客户端返回JSON响应
  data = {'ename':'丁当', 'isMarried':True}
  res = JsonResponse( data )  #此处会自动执行JSON序列化，把dict/list转换为JSON字符串
  res['Access-Control-Allow-Origin'] = '*'
  return res

#路由方法：处理客户端的“商品详情”请求
def  productDetail( req, pid ):
  print(type(pid))
  print(pid)
  res = HttpResponse('<h3>商品详情</h3><hr>')
  return res
