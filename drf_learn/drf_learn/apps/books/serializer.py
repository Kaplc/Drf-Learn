from rest_framework import serializers


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
    bread = serializers.IntegerField(label='阅读量', required=False, read_only=True, max_value=2)  # 不进行验证和保存,直接返回
    bcomment = serializers.IntegerField(label='评论量', required=False, write_only=True, max_value=10)  # 只进行验证和保存,不返回
    image = serializers.ImageField(label='图片', required=False)

    # ----------------------------返回关联的外键数据------------------------- #
    # PrimaryKeyRelatedField--返回的是外键的id
    # 字段名因为设置了relate_name=heroes, 否则使用heroinfo_set
    # heroes = serializers.PrimaryKeyRelatedField(label='包含人物', read_only=True, many=True)

    # StringRelatedField--返回的是外键的模型的__str__方法返回的值
    # heroes = serializers.StringRelatedField(label='包含人物', read_only=True, many=True)

    # 嵌套序列化器
    # heroes = HeroInfoSerializer(many=True)
