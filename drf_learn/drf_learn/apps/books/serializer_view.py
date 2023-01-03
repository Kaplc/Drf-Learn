import json

from django.views import View
from .models import BookInfo
from .serializer import BookInfoSerializer
from django.http import JsonResponse


class Books(View):
    """多个对象"""

    def get(self, request):
        # 查询所有图书对象
        books = BookInfo.objects.all()
        # 创建序列化器对象, 传入查询集
        # many=True--多个对象返回
        ser = BookInfoSerializer(books, many=True)
        # ser.data--获取序列化完成的数据
        # safe=False--多对象使用
        return JsonResponse(ser.data, safe=False)

    def post(self, request):
        # 获取数据并转成字典
        data = request.body.decode()
        data_dict = json.loads(data)
        # 序列化器验证数据
        ser = BookInfoSerializer(data=data_dict)
        ser.is_valid()  # 调用序列化器的验证方法
        print(ser.errors)  # 验证失败的提示
        print(ser.validated_data)  # 验证成功后的数据
        return JsonResponse(ser.validated_data, safe=False)


class Book(View):
    """单一对象"""

    def get(self, request):
        # 查询单个图书对象
        books = BookInfo.objects.get(id=1)
        # 创建序列化器对象, 传入查询单个结果
        ser = BookInfoSerializer(books)
        # ser.data--获取序列化完成的数据
        return JsonResponse(ser.data)
