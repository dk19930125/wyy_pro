
from rest_framework import serializers


from .models import SKU

class SKUSerializer(serializers.ModelSerializer):

    class Meta:
        model = SKU
        fields = ('id', 'name', 'vendor', 'price', 'source_url', 'image_url', 'dt')