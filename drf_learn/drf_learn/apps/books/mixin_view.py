from .models import BookInfo
from .serializer import BookInfoSerializer, BookModelSerializer
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.mixins import CreateModelMixin, ListModelMixin, UpdateModelMixin, DestroyModelMixin, \
    RetrieveModelMixin


class Books(GenericAPIView, CreateModelMixin, ListModelMixin):
    """多个对象"""
    queryset = books = BookInfo.objects.all()  # 先定义查询集
    serializer_class = BookInfoSerializer  # 定义序列化器

    def get(self, request):
        return self.list(request)  # 使用DRF的ListModelMixin的list方法, 自动返回所有数据

    def post(self, request):
        return self.create(request)  # # 使用DRF的CreateModelMixin的create方法, 保存数据


class Book(GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
    """单一对象"""
    queryset = books = BookInfo.objects.all()  # 先定义查询集
    serializer_class = BookInfoSerializer  # 定义序列化器

    def get(self, request, pk):
        return self.retrieve(request, pk)

    def put(self, request, pk):
        return self.update(request, pk)

    def delete(self, request, pk):
        return self.destroy(request, pk)
