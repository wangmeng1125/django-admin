from django.db import models

# Create your models here.
from dvadmin.utils.models import CoreModel

class DataTargetModel(CoreModel):
    model = models.CharField(max_length=255, verbose_name="模型")
    dataset= models.CharField(max_length=255, verbose_name="数据集")

    Validation_mIoU = models.FloatField(verbose_name="Validation_mIoU")
    Test_Score = models.FloatField(verbose_name="Test_Score")
    params_M = models.FloatField(verbose_name="params_M")
    GFLOPs_512 = models.FloatField(verbose_name="GFLOPs_512")

    version = models.FloatField(verbose_name="版本号")
    algorithm_create_date = models.DateField(verbose_name="创建时间")
    creater = models.CharField(max_length=255, verbose_name="创建人")

    class Meta:
        db_table = "targets"
        verbose_name = '算法表'
        verbose_name_plural = verbose_name
        ordering = ('-create_datetime',)