from django.urls import path, include
from rest_framework.routers import SimpleRouter

from .views import (GetProductView,
                    UpdateProductView, DestroyProductView,
                    LikeProductView, ReviewViewSet,
                    FavouriteProductView, FavouriteListView,
                    ProductImageView, ListProductView, CreateProductView)


router = SimpleRouter()
router.register('reviews', ReviewViewSet)
router.register('product_images', ProductImageView)


urlpatterns = [
    path('list/', ListProductView.as_view()),
    path('create/', CreateProductView.as_view()),
    path('<int:pk>/', GetProductView.as_view()),
    path('delete/<int:pk>/', DestroyProductView.as_view()),
    path('update/<int:pk>/', UpdateProductView.as_view()),
    path('<int:pk>/like/', LikeProductView.as_view()),
    path('favourites/', FavouriteListView.as_view()),
    path('<int:pk>/favourite/', FavouriteProductView.as_view()),
    path('', include(router.urls)),
]
