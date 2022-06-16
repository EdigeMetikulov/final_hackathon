from django.shortcuts import get_object_or_404
from rest_framework import generics, status, viewsets
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, AllowAny, IsAdminUser
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, filters
from django.db.models import Q

from .models import Product, LikeProduct, Review, FavProduct, ProductImage
from .permissions import IsAuthorOrAdminPermission
from .serializers import (ProductSerializer, LikeProductSerializer,
                          ReviewSerializer, ProductDetailSerializer,
                          FavouriteSerializer, ProductImageSerializer)
from .paginations import ProductPagination


class ListProductView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (AllowAny,)
    pagination_class = ProductPagination
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['is_published', 'price', 'category']
    search_fields = ['title', 'price']

    # def get_serializer_context(self):
    #     return super().get_serializer_context()


class CreateProductView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (IsAdminUser,)

    # def get_serializer_context(self):
    #     return super().get_serializer_context()


class GetProductView(APIView):

    def get(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        product.watch += 1
        product.save()
        serializer = ProductDetailSerializer(product)
        return Response(serializer.data)


class DestroyProductView(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class UpdateProductView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class LikeProductView(APIView):

    permission_classes = (IsAuthenticated,)

    def get(self, request, pk):
        user = request.user
        product = get_object_or_404(Product, pk=pk)
        like, create = LikeProduct.objects.get_or_create(user=user, product=product)
        if like.is_like:  #если тру
            like.is_like = False  #становится фолс
            like.save()
        else:  # если фолс
            like.is_like = True
            like.save()

        serializer = LikeProductSerializer(like)
        return Response(serializer.data)


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def get_permissions(self):
        if self.action == 'retrieve':
            return []
        if self.action == 'create':
            return [IsAuthenticated()]
        # update, partial_update, destroy
        return [IsAuthorOrAdminPermission()]


class ProductImageView(viewsets.ModelViewSet):
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageSerializer


class FavouriteListView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = FavouriteSerializer
    permission_classes = [IsAuthenticated, ]

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(favourites__user=self.request.user, favourites__is_fav=True)
        return queryset


class FavouriteProductView(APIView):
    permission_classes = [IsAuthenticated, ]

    def get(self, request, pk):
        user = request.user
        product = get_object_or_404(Product, pk=pk)
        fav, create = FavProduct.objects.get_or_create(user=user, product=product)
        if not fav.is_fav:
            fav.is_fav = not fav.is_fav
            fav.save()
            return Response('This product was added to favourites')
        else:
            fav.is_fav = not fav.is_fav
            fav.save()
            return Response('This product was removed from favourites')

        # serializer = FavouriteSerializer(fav)
        # return Response(serializer.data)
