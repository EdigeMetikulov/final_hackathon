from rest_framework import serializers

from .models import (Product, LikeProduct,
                     Review, FavProduct,
                     ProductImage)


class ProductSerializer(serializers.ModelSerializer):
    # owner = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Product
        fields = ['id', 'title', 'category', 'price', 'watch', "image"]

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['category'] = instance.category
        # representation['owner'] = instance.owner.email
        representation['likes'] = instance.likes.all().count()
        representation['reviews'] = instance.reviews.all().count()
        if representation["image"] and "http" in representation['image']:
            representation['image'] = representation["image"][representation["image"].index("https"):].replace("%3A", r":/")
        return representation


class ProductDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['category'] = instance.category
        # representation['owner'] = instance.owner.email
        representation['likes'] = instance.likes.filter(is_like=True).count()
        representation['reviews'] = ReviewSerializer(instance.reviews.all(), many=True).data
        if representation["image"] and "http" in representation['image']:
            representation['image'] = representation["image"][representation["image"].index("http"):].replace("%3A", r":/")
        return representation


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        exclude = ('author',)

    def validate(self, attrs):
        request = self.context.get('request')
        attrs['author'] = request.user
        return attrs

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['product'] = instance.product.title
        representation['author'] = instance.author.email
        return representation


class LikeProductSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = LikeProduct
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['product'] = instance.product.title
        return representation


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['product'] = instance.product.title
        return representation


class FavouriteSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Product
        fields = ['id', 'title', 'price', 'image', 'category', 'user']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['category'] = instance.category
        return representation



