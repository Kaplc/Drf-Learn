"""
5个mixin和genericview的集合
self.action当前的方法
"""
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.throttling import UserRateThrottle
from rest_framework.viewsets import ModelViewSet
from books.models import BookInfo
from books.serializer import BookInfoSerializer


class Books(ModelViewSet):
    """多个对象"""
    permission_classes = (IsAuthenticated,)  # 设置权限

    throttle_classes = (UserRateThrottle,)  # 设置限流  AnonRateThrottle限制所有匿名未认证用户，使用IP区分用户,
    # UserRateThrottle限制认证用户，使用User id 来区分

    filterset_fields = ('btitle',)  # 设置过滤字段

    queryset = books = BookInfo.objects.all()  # 先定义查询集
    serializer_class = BookInfoSerializer  # 定义序列化器

    def get_serializer_class(self):
        """不同方法用不同的序列化器"""
        if self.action == 'test':  # self.action当前的方法
            return BookInfoSerializer
        else:
            return BookInfoSerializer

    @action(methods=['get'], detail=True)  # 自定义方法使用自动生成路由, detail==True--生成pk匹配路由
    def test(self, request, pk):
        ser = self.get_serializer_class()


class Book(ModelViewSet):
    """单一对象"""
    queryset = books = BookInfo.objects.all()  # 先定义查询集
    serializer_class = BookInfoSerializer  # 定义序列化器
