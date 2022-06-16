from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics

from .models import Category
from .serializers import CategorySerializer
# from .permission import IsAdminOrAllowAny
from rest_framework.permissions import IsAdminUser, AllowAny
from rest_framework import generics, filters

from ..product.models import Product


class ListCategoryView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (AllowAny,)



class CreateCategoryView(generics.CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (IsAdminUser,)


