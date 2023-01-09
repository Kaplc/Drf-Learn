from django.urls import re_path
from .view import serializer_view, generic_view, child_view, mixin_view, api_view, viewset_view

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
    re_path(r'gvsbooks$', viewset_view.Books.as_view({'get': 'list', 'post': 'create'})),
    # genericviewset
    re_path(r'gvsook/(?P<pk>\d)$', viewset_view.Book.as_view({'get': 'retrieve', 'put': 'updata'})),
    # genericviewset自定义方法名匹配
    re_path(r'gvsbooks/test$', viewset_view.Books.as_view({'get': 'list', 'post': 'create', 'put': 'test'})),
]
