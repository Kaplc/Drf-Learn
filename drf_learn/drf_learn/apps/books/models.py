from django.db import models

# Create your models here.
from django.db.models import PROTECT


class BookInfo(models.Model):
    btitle = models.CharField(max_length=20, verbose_name='名称')
    bpub_date = models.DateField(verbose_name='发布日期', null=True)
    bread = models.IntegerField(default=0, verbose_name='阅读量')
    bcomment = models.IntegerField(default=0, verbose_name='评论量')
    image = models.ImageField(upload_to='booktest', verbose_name='图片', null=True)

    def __str__(self):
        return self.btitle

class HeroInfo(models.Model):
    book = models.ForeignKey(BookInfo, on_delete=PROTECT, related_name='heroes', verbose_name='书名')
    name = models.CharField(max_length=20, verbose_name='名子')

    def __str__(self):
        return self.name
