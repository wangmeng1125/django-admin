from django.shortcuts import render

from data_target.models import DataTargetModel
from data_target.serializers import DataTargetModelSerializer, DataTargetModelCreateUpdateSerializer
from dvadmin.utils.viewset import CustomModelViewSet

class DataTargetModelViewSet(CustomModelViewSet):
    """
    list:查询
    create:新增
    update:修改
    retrieve:单例
    destroy:删除
    """
    queryset = DataTargetModel.objects.all()
    serializer_class = DataTargetModelSerializer
    create_serializer_class = DataTargetModelCreateUpdateSerializer
    update_serializer_class = DataTargetModelCreateUpdateSerializer
    filter_fields = ['model', 'dataset']
    search_fields = ['model']
