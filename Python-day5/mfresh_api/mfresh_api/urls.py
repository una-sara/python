from django.contrib import admin
from django.urls import path
from user.views import userLogin, userRegister, userCheckUname, userCheckPhone
from news.views import newsList, newsDetail

#####测试用的路由处理函数######
from django.http import HttpResponse
from user.models import MfUser

def  testInsert(req):
    #MfUser.objects：是ORM框架提供的数据库操作映射对象
    u = MfUser.objects.create(uname='yaya', upwd='456', phone='13501111112')
    print(u.uid, u.uname, u.upwd, u.phone)

    res = HttpResponse('正在测试INSERT....')
    return res


def  testDelete(req):
    #MfUser.objects.delete()  #DELETE FROM  mf_user;
    result = MfUser.objects.filter(uid=3).delete()
    print( type(result) )
    print( result )

    res = HttpResponse('正在测试DELETE....')
    return res


def  testUpdate(req):
    n = MfUser.objects.filter(uid=444).update(uname='yayaya',upwd='666')
    print( n )

    res = HttpResponse('正在测试Update....')
    return res


def  testSelectOne(req):
    result = MfUser.objects.filter(uid=111).values('uname', 'upwd', 'phone')
    print( type(result) )
    print( result ) 

    res = HttpResponse('正在测试SelectOne....')
    return res


def  testSelectAll(req):
    result = MfUser.objects.values('uname', 'upwd', 'phone')
    print( type(result) )
    print( result ) 

    res = HttpResponse('正在测试SelectAll....')
    return res
#############################

urlpatterns = [         
    path('test/insert', testInsert),
    path('test/delete', testDelete),
    path('test/update', testUpdate),
    path('test/select/one', testSelectOne),
    path('test/select/all', testSelectAll),

    path('admin/', admin.site.urls),
    path('user/login', userLogin),
    path('user/register', userRegister),
    path('user/check/uname', userCheckUname),
    path('user/check/phone', userCheckPhone),
   
    path('news/list', newsList),
    path('news/detail', newsDetail),
]
