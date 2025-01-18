from rest_framework.serializers import ModelSerializer
from .models import Members


class FromSerializer(ModelSerializer):
    class Meta:
        model = Members
        fields = '__all__'

