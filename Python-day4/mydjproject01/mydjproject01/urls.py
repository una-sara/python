from django.contrib import admin
from django.urls import path
from django.http import HttpResponse

'''
#路由方法 ——  View(MTV中的V)
def doLogin(req):
    print('服务器接收到一个HTTP请求')
    print('doLogin方法正在处理')
    res = HttpResponse('<h2>WELCOME</h2><hr>')
    return res

def doRegister(req):
    res = HttpResponse('<h2>REGISTER SUCC</h2><hr><hr>')
    return res

#路由词典：指定每个请求地址，该由哪个函数来处理
urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', doLogin),
    path('user/register', doRegister),
]
'''

#主App下导入其它包时，无需添加“上一级目录下”的..
from user.views import userLogin, userRegister
from product.views import productList, productDetail

#路由词典
urlpatterns = [
    path('user/login', userLogin),
    path('user/register', userRegister),
    path('product/list', productList),
    path('product/detail/<int:pid>', productDetail),
]