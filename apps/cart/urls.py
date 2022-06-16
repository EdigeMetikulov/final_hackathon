from django.urls import path

from .views import AddProductInCartView, ShoppingCartView, ShoppingCartUpdateView, ShoppingCartDeleteView

urlpatterns = [
    path('', ShoppingCartView.as_view()),
    path('add/', AddProductInCartView.as_view()),
    path('put/<int:pk>/', ShoppingCartUpdateView.as_view()),
    path('delete/<int:pk>/', ShoppingCartDeleteView.as_view()),

]

