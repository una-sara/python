#使用Python系统模块——http.client

import http.client

#使用Python向学子商城服务器发起HTTP请求

#①向目标服务器创建连接
conn = http.client.HTTPConnection('www.codeboy.com')
#②发起GET请求
conn.request('GET', '/css/slide.css')
#③获取服务器端返回的响应消息
res = conn.getresponse()
print('响应状态码：', res.status)
print('原因短句：', res.reason)
#④读取响应主体
body = res.read()
print(body)