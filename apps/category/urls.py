from django.urls import path

from .views import ListCategoryView, CreateCategoryView

urlpatterns = [
    path('list/', ListCategoryView.as_view()),
    path('create/', CreateCategoryView.as_view()),

]