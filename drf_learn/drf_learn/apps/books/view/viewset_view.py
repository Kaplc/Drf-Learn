"""
viewset-继承APIView
可以自定义方法名
"""
from rest_framework.viewsets import ViewSet
from books.models import BookInfo
from books.serializer import BookInfoSerializer, BookModelSerializer
from rest_framework.response import Response


class Books(ViewSet):
    """多个对象"""

    def list(self, request):

        # 查询所有图书对象
        books = BookInfo.objects.all()
        # 创建序列化器对象, 传入查询集
        # many=True--多个对象返回
        ser = BookInfoSerializer(books, many=True)

        # ser.data--获取序列化完成的数据
        return Response(ser.data)  # 使用DRF的Response

    def create(self, request):
        # 获取数据并转成字典
        # data = request.body.decode()
        # data_dict = json.loads(data)
        # DRF获取前端数据
        data_dict = request.data
        # 序列化器验证数据
        ser = BookInfoSerializer(data=data_dict)
        ser.is_valid()  # 调用序列化器的验证方法
        print(ser.errors)  # 验证失败的提示
        print(ser.validated_data)  # 验证成功后的数据

        # 保存数据
        ser.save()

        return Response(ser.validated_data)

    def test(self, request):
        return Response({'ok'})


class Book(ViewSet):
    """单一对象"""

    def retrieve(self, request, pk):
        print(request.query_params)  # 使用DRF获取参数
        # 查询单个图书对象
        book = BookInfo.objects.get(id=pk)
        # 创建序列化器对象, 传入查询单个结果
        ser = BookInfoSerializer(book)
        # ser.data--获取序列化完成的数据
        return Response(ser.data)

    def updata(self, request, pk):
        # 获取数据并转成字典
        data_dict = request.data
        # 验证
        try:
            book = BookInfo.objects.get(id=pk)
        except:
            return Response({'error': '信息错误'}, status=400)
        ser = BookInfoSerializer(instance=book, data=data_dict)
        model_ser = BookModelSerializer(instance=book, data=data_dict)  # 模型类序列化器
        model_ser.is_valid()
        ser.is_valid()
        # 更新数据
        ser.save()

        return Response(ser.validated_data)
