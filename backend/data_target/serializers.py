from data_target.models import DataTargetModel
from dvadmin.utils.serializers import CustomModelSerializer


class DataTargetModelSerializer(CustomModelSerializer):
    """
    序列化器
    """

    class Meta:
        model = DataTargetModel
        fields = "__all__"


class DataTargetModelCreateUpdateSerializer(CustomModelSerializer):
    """
    创建/更新时的列化器
    """

    class Meta:
        model = DataTargetModel
        fields = '__all__'