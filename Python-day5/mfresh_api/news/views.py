from django.http import JsonResponse
from .models import MfNews
import math

'''
2.1按发布时间逆序返回新闻列表
API地址：	/news/list
处理方法：	newsList( req )
请求方法：	GET
请求参数：	查询字符串：
pageNum-需显示的页号；可选，默认为1
响应结果：	{
    totalRecord: 58,
    pageSize: 10,
    pageCount: 6,
    pageNum: 1,
    data: [{"nid":1,"title":"新闻标题","pubtime":"1234"},{} ... {}]
}
'''
def  newsList(req):
  #读取请求数据
  pno = req.GET.get('pageNum', 1)
  pno = int(pno) #要查询的分页号
  output = {
    'totalRecord':  0,      #总记录数
    'pageSize':     10,     #页面大小
    'pageCount':    0,      #总页数
    'pageNum':      pno,    #当前显示的页号
    'data':         [],     #当前页中的数据
  }
  #执行数据库查询操作，获得总的记录数
  #select count(*) from mf_news
  count = MfNews.objects.count()
  output['totalRecord'] = count
  #根据总记录数以及页面大小计算总页数
  output['pageCount'] = math.ceil( output['totalRecord'] / output['pageSize'])
  #查询指定页面中的记录
  #select nid,title,pubtime from mf_news  order by pubtime desc  limit ?,?
  result = MfNews.objects.order_by('-pubtime').values('nid','title', 'pubtime')
  start = (output['pageNum']-1)*output['pageSize']
  end = output['pageNum']*output['pageSize']
  result = result[start : end]
  result = list(result)#QuerySet必须转化为list才能序列化
  output['data'] = result
  #返回响应消息
  res = JsonResponse(output)
  res['Access-Control-Allow-Origin'] = '*'
  return res

'''
2.2根据新闻ID返回新闻详情
API地址：	/news/detail
处理方法：	newsDetail( req )
请求方法：	GET
请求参数：	查询字符串：
nid-新闻ID，必需
响应结果：	{
    "nid": 1,
    "title":"新闻标题",
    "pubtime":1234,
    "content":"新闻内容"
}
'''
def  newsDetail(req):
  #读取请求数据
  i = req.GET.get('nid')
  #执行数据库查询操作select * from mf_news where nid=?
  result = MfNews.objects.filter(nid=i).values()
  news = result[0]  #从QuerySet中读取第一个新闻对象
  #返回响应消息
  res = JsonResponse( news )#QuerySet中取出的数据是dict
  res['Access-Control-Allow-Origin'] = '*'
  return res