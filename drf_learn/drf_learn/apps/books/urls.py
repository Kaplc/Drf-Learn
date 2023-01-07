from django.urls import re_path
from . import serializer_view
from . import api_view
from . import generic_view
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
]
