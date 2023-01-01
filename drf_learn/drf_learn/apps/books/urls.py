from django.urls import re_path
from .serializer_view import *

urlpatterns = [
    # 多对象
    re_path(r'books$', Books.as_view()),
    # 单对象
    re_path(r'book$', Books.as_view())
]
