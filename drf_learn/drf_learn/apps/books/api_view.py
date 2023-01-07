import json
from django.views import View
from .models import BookInfo
from .serializer import BookInfoSerializer, BookModelSerializer
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response


class Books(APIView):
    """多个对象"""

    def get(self, request):

        # 查询所有图书对象
        books = BookInfo.objects.all()
        # 创建序列化器对象, 传入查询集
        # many=True--多个对象返回
        ser = BookInfoSerializer(books, many=True)

        # ser.data--获取序列化完成的数据
        return Response(ser.data)  # 使用DRF的Response

    def post(self, request):
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


class Book(APIView):
    """单一对象"""

    def get(self, request, pk):
        print(request.query_params)  # 使用DRF获取参数
        # 查询单个图书对象
        book = BookInfo.objects.get(id=pk)
        # 创建序列化器对象, 传入查询单个结果
        ser = BookInfoSerializer(book)
        # ser.data--获取序列化完成的数据
        return JsonResponse(ser.data)

    def put(self, request, pk):
        # 获取数据并转成字典
        data = request.body.decode()
        data_dict = json.loads(data)
        # 验证
        try:
            book = BookInfo.objects.get(id=pk)
        except:
            return JsonResponse({'error': '信息错误'}, status=400)
        ser = BookInfoSerializer(instance=book, data=data_dict)
        model_ser = BookModelSerializer(instance=book, data=data_dict)  # 模型类序列化器
        model_ser.is_valid()
        ser.is_valid()
        # 更新数据
        ser.save()

        return JsonResponse(ser.validated_data)
