from django.db import models

# 定义数据格式
from dvadmin.utils.models import CoreModel

class CrudDemoModel(CoreModel):
    goods = models.CharField(max_length=255, verbose_name="商品")
    inventory = models.IntegerField(verbose_name="库存量")
    goods_price = models.FloatField(verbose_name="商品定价")
    purchase_goods_date = models.DateField(verbose_name="进货时间")

    class Meta:
        db_table = "goods"                  # 数据库中的表名goods
        verbose_name = '商品表'              # goods
        verbose_name_plural = verbose_name
        ordering = ('-create_datetime',)