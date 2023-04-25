from django.shortcuts import render

from data_visual.models import DataVisualModel
from data_visual.serializers import DataVisualModelSerializer, DataVisualModelCreateUpdateSerializer
from dvadmin.utils.viewset import CustomModelViewSet

class DataVisualModelViewSet(CustomModelViewSet):
    """
    list:查询
    create:新增
    update:修改
    retrieve:单例
    destroy:删除
    """
    queryset = DataVisualModel.objects.all()
    serializer_class = DataVisualModelSerializer
    create_serializer_class = DataVisualModelCreateUpdateSerializer
    update_serializer_class = DataVisualModelCreateUpdateSerializer
    filter_fields = ['algorithm', 'dataset']
    search_fields = ['algorithm']
