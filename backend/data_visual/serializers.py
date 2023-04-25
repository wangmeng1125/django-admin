from data_visual.models import DataVisualModel
from dvadmin.utils.serializers import CustomModelSerializer


class DataVisualModelSerializer(CustomModelSerializer):
    """
    序列化器
    """

    class Meta:
        model = DataVisualModel
        fields = "__all__"


class DataVisualModelCreateUpdateSerializer(CustomModelSerializer):
    """
    创建/更新时的列化器
    """

    class Meta:
        model = DataVisualModel
        fields = '__all__'