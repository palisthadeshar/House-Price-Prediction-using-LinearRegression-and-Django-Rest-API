from rest_framework import serializers
from .models import price


#convert price model instances to JSON format, which can be sent over the network in response to API requests
class priceSerializers(serializers.ModelSerializer):
    class Meta:
        model=price
        fields='__all__'