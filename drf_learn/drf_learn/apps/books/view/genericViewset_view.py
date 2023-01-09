"""
继承genericview
路由匹配跟viewset一样
"""
from books.models import BookInfo
from books.serializer import BookInfoSerializer, BookModelSerializer
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet


class Books(GenericViewSet):
    """多个对象"""
    queryset = books = BookInfo.objects.all()  # 先定义查询集
    serializer_class = BookInfoSerializer  # 定义序列化器

    def list(self, request):
        # 查询所有图书对象
        books = self.get_queryset()  # 获取指定查询集的数据
        # 使用指定的序列化器对象, 传入查询集
        ser = self.get_serializer(instance=books, many=True)

        # ser.data--获取序列化完成的数据
        return Response(ser.data)  # 使用DRF的Response

    def create(self, request):
        # 获取数据并转成字典
        # data = request.body.decode()
        # data_dict = json.loads(data)
        # DRF获取前端数据
        data_dict = request.data
        # 使用指定的序列化器对象, 传入数据
        ser = self.get_serializer(data=data_dict)
        ser.is_valid()  # 调用序列化器的验证方法
        print(ser.errors)  # 验证失败的提示
        print(ser.validated_data)  # 验证成功后的数据

        # 保存数据
        ser.save()

        return Response(ser.validated_data)


class Book(GenericViewSet):
    """单一对象"""
    queryset = books = BookInfo.objects.all()  # 先定义查询集
    serializer_class = BookInfoSerializer  # 定义序列化器

    def retrieve(self, request, pk):
        print(request.query_params)  # 使用DRF获取参数
        # 查询单个图书对象
        book = self.get_object()  # 从定义的查询集中获取指定的数据对象
        # 创建序列化器对象, 传入查询单个结果
        ser = self.get_serializer(instance=book)
        # ser.data--获取序列化完成的数据
        return Response(ser.data)

    def updata(self, request, pk):
        # 获取数据并转成字典
        data_dict = request.data
        # 验证
        try:
            book = self.get_object()  # 从定义的查询集中获取指定的数据对象
        except:
            return Response({'error': '信息错误'}, status=400)
        ser = BookInfoSerializer(instance=book, data=data_dict)
        model_ser = BookModelSerializer(instance=book, data=data_dict)  # 模型类序列化器
        model_ser.is_valid()
        ser.is_valid()
        # 更新数据
        ser.save()

        return Response(ser.validated_data)
