from rest_framework import serializers
from ..models import Product


class ProductSerializer(serializers.ModelSerializer):
    title = serializers.CharField()
    description = serializers.CharField()
    parameters = serializers.JSONField()

    class Meta:
        model = Product
        fields = [
            "id", "title", "description", "parameters"
        ]
