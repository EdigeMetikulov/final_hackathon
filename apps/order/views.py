from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework import viewsets

from apps.order.models import Order
from apps.order.serializers import OrderSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    # def get_permissions(self):
    #     if self.action == 'retrieve':
    #         return []
    #     if self.action == 'create':
    #         return [IsAuthenticated()]
    #     # update partialupdate destroy
    #     return [IsAuthorOrAdminPermission()]