from rest_framework import serializers
from .models import Item

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ["id", "name", "owner"]

    def update(self, instance, validated_data):
        validated_data.pop("owner", None)
        return super().update(instance, validated_data)
