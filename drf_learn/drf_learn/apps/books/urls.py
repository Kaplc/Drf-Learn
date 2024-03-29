from django.urls import re_path
from rest_framework.routers import SimpleRouter

from .view import serializer_view, generic_view, child_view, mixin_view, api_view, viewset_view, genericViewset_view, \
    modelviewset

urlpatterns = [
    # 多对象
    re_path(r'books$', serializer_view.Books.as_view()),
    # 单对象
    re_path(r'book/(?P<pk>\d)$', serializer_view.Book.as_view()),

    # APIView多对象
    re_path(r'apibooks$', api_view.Books.as_view()),
    # APIView单对象
    re_path(r'apibook/(?P<pk>\d)$', api_view.Book.as_view()),

    # genericView多对象
    re_path(r'gnbooks$', generic_view.Books.as_view()),
    # genericView单对象
    re_path(r'gnbook/(?P<pk>\d)$', generic_view.Book.as_view()),

    # genericView多对象+mixin
    re_path(r'mxbooks$', mixin_view.Books.as_view()),
    # genericView单对象+mixin
    re_path(r'mxbook/(?P<pk>\d)$', mixin_view.Book.as_view()),

    # genericView多对象+mixin集合子类
    re_path(r'chbooks$', child_view.Books.as_view()),
    # genericView单对象+mixin集合子类
    re_path(r'chbook/(?P<pk>\d)$', child_view.Book.as_view()),

    # viewset
    re_path(r'vsbooks$', viewset_view.Books.as_view({'get': 'list', 'post': 'create'})),
    # viewset
    re_path(r'vsbook/(?P<pk>\d)$', viewset_view.Book.as_view({'get': 'retrieve', 'put': 'updata'})),
    # viewset自定义方法名匹配
    re_path(r'vsbooks/test$', viewset_view.Books.as_view({'get': 'list', 'post': 'create', 'put': 'test'})),

    # genericviewset
    re_path(r'gvsbooks$', genericViewset_view.Books.as_view({'get': 'list', 'post': 'create'})),
    # genericviewset
    re_path(r'gvsook/(?P<pk>\d)$', genericViewset_view.Book.as_view({'get': 'retrieve', 'put': 'updata'})),
    # genericviewset自定义方法名匹配
    re_path(r'gvsbooks/test$', genericViewset_view.Books.as_view({'get': 'list', 'post': 'create', 'put': 'test'})),

    # modelviewset
    re_path(r'mdbooks$', modelviewset.Books.as_view({'get': 'list', 'post': 'create'})),
    # modelviewset
    re_path(r'mdsook/(?P<pk>\d)$', modelviewset.Book.as_view({'get': 'retrieve', 'put': 'updata'})),
]

# 自动生成路由
router = SimpleRouter()  # 创建对象
router.register('zdybooks', modelviewset.Books, basename='books')  # 路径+调用的方法+路由命名
router.register('zdyffbooks', modelviewset.Books)
urlpatterns += router.urls  # 自动生成的路由添加到路由列表
print(urlpatterns)

