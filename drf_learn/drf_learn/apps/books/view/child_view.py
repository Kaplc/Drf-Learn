from books.models import BookInfo
from books.serializer import BookInfoSerializer, BookModelSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView


class Books(ListCreateAPIView):
    """多个对象"""
    queryset = books = BookInfo.objects.all()  # 先定义查询集
    serializer_class = BookInfoSerializer  # 定义序列化器


class Book(RetrieveUpdateDestroyAPIView):
    """单一对象"""
    queryset = books = BookInfo.objects.all()  # 先定义查询集
    serializer_class = BookInfoSerializer  # 定义序列化器
