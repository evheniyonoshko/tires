from rest_framework import serializers

from tiresapp.models import Tire


class TireSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tire
        fields = ('id', 'name', 'width', 'height', 'diameter', 'speed_index', 'picture')
