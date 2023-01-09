"""
5个mixin和genericview的集合

"""
from rest_framework.viewsets import ModelViewSet
from books.models import BookInfo
from books.serializer import BookInfoSerializer


class Books(ModelViewSet):
    """多个对象"""
    queryset = books = BookInfo.objects.all()  # 先定义查询集
    serializer_class = BookInfoSerializer  # 定义序列化器


class Book(ModelViewSet):
    """单一对象"""
    queryset = books = BookInfo.objects.all()  # 先定义查询集
    serializer_class = BookInfoSerializer  # 定义序列化器