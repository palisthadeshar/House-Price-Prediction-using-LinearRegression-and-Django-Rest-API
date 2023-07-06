from rest_framework import serializers
from .models import price

class priceSerializers(serializers.ModelSerializer):
    class Meta:
        model=price
        fields='__all__'