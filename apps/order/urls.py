from django.urls import path, include
from rest_framework.routers import SimpleRouter

from apps.order.views import OrderViewSet

router = SimpleRouter()

router.register('', OrderViewSet)


urlpatterns = [
    path('', include(router.urls)),

]
