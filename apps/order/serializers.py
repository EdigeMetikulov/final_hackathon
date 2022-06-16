from rest_framework import serializers

from apps.order.models import Order


class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = "__all__"

    # def to_representation(self, instance):
    #     rep = super().to_representation(instance)
    #     rep["category"] = instance.category.title
    #     rep["likes"] = instance.likes.all().count()
    #     return rep