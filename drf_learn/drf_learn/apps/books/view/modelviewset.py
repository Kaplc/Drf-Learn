"""
5个mixin和genericview的集合

"""
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet
from books.models import BookInfo
from books.serializer import BookInfoSerializer


class Books(ModelViewSet):
    """多个对象"""
    queryset = books = BookInfo.objects.all()  # 先定义查询集
    serializer_class = BookInfoSerializer  # 定义序列化器

    @action(methods=['get'], detail=True)  # 自定义方法使用自动生成路由, detail==True--生成pk匹配路由
    def test(self, request, pk):
        pass


class Book(ModelViewSet):
    """单一对象"""
    queryset = books = BookInfo.objects.all()  # 先定义查询集
    serializer_class = BookInfoSerializer  # 定义序列化器
