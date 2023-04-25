from django.db import models

# Create your models here.
from dvadmin.utils.models import CoreModel

class DataVisualModel(CoreModel):
    algorithm = models.CharField(max_length=255, verbose_name="算法")
    model = models.CharField(max_length=255, verbose_name="模型")
    dataset= models.CharField(max_length=255, verbose_name="数据集")
    epoch = models.IntegerField(verbose_name="学习轮数")
    learning_rate = models.FloatField(verbose_name="学习率")
    version = models.FloatField(verbose_name="版本号")
    algorithm_create_date = models.DateField(verbose_name="创建时间")

    class Meta:
        db_table = "algorithms"
        verbose_name = '算法表'
        verbose_name_plural = verbose_name
        ordering = ('-create_datetime',)