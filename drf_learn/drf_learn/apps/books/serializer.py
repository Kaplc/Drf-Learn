from rest_framework import serializers
from books.models import BookInfo


# 嵌套序列化器
class HeroInfoSerializer(serializers.Serializer):
    """嵌套序列化器"""
    name = serializers.CharField()
    book = serializers.StringRelatedField()


# 自定义序列化器
class BookInfoSerializer(serializers.Serializer):
    """图书数据序列化器(数据->json)"""
    # IntegerField, CharField等--字段类型
    # label--用于HTML展示API页面时，显示的字段名称
    # ----序列化器验证方法的选项参数----
    # read_only--表明该字段仅用于序列化输出，默认False, 不进行验证和保存,直接返回
    # write_only--表明该字段仅用于序列化输出，默认False, 只进行验证和保存,不返回
    # required--表明该字段在反序列化时必须输入，默认True
    # max_length--最大长度
    id = serializers.IntegerField(label='ID', read_only=True)
    btitle = serializers.CharField(label='名称', max_length=20)
    bpub_data = serializers.DateField(label='发布日期', required=False)
    bread = serializers.IntegerField(label='阅读量', required=False, max_value=10)  # read_only=True 不进行验证和保存,直接返回
    bcomment = serializers.IntegerField(label='评论量', required=False, max_value=10)  # write_only只进行验证和保存,不返回
    image = serializers.ImageField(label='图片', required=False)

    # ----------------------------返回关联的外键数据------------------------- #
    # PrimaryKeyRelatedField--返回的是外键的id
    # 字段名因为设置了relate_name=heroes, 否则使用heroinfo_set
    # heroes = serializers.PrimaryKeyRelatedField(label='包含人物', read_only=True, many=True)

    # StringRelatedField--返回的是外键的模型的__str__方法返回的值
    # heroes = serializers.StringRelatedField(label='包含人物', read_only=True, many=True)

    # 嵌套序列化器
    # heroes = HeroInfoSerializer(many=True)

    # --------------------------自定义验证方法--------------------------- #
    def validate_btitle(self, attrs):
        """单一字段验证"""
        if attrs == 'python':
            raise serializers.ValidationError('书名不能是python')

        return attrs

    def validate(self, attrs):
        """多个字段验证"""
        if attrs['bread'] < attrs['bcomment']:
            raise serializers.ValidationError('评论量大于阅读量')
        return attrs

    # --------------------------反序列化保存方法--------------------------- #
    def create(self, validated_data):
        """
        保存方法
        :param validated_data: 要保存的数据对象
        :return:
        """
        # 保存数据
        book = BookInfo.objects.create(**validated_data)
        return book

    # --------------------------反序列化更新方法--------------------------- #
    def update(self, instance, validated_data):
        """
        更新方法
        :param instance: 原数据对象
        :param validated_data: 要更新的数据对象
        :return:
        """
        instance.btitle = validated_data['btitle']
        instance.bread = validated_data['bread']
        instance.save()
        return instance


class BookModelSerializer(serializers.ModelSerializer):
    """模型类序列化器"""
    bread = serializers.IntegerField(min_value=1)  # 指定字段后修改选项参数, 要手动再定义字段

    class Meta:
        model = BookInfo  # 指定模型类
        fields = ('btitle', 'bread')  # 指定字段
        # fields = '__all__'  # 所有字段
        # exclude = ('btitle',)  # 取反
