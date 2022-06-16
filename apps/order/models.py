from django.db import models

from apps.cart.models import ShoppingCart


class Order(models.Model):
    PAY_CHOICES = (
        ("cash", "Наличными"),
        ("card", "Оплата картой"),
        ("debt", "В долг")
    )
    shopping_cart = models.ForeignKey(to=ShoppingCart, on_delete=models.CASCADE, related_name='order')
    phone_number = models.CharField(max_length=13)
    address = models.TextField()
    email = models.EmailField()
    pay_choices = models.CharField(choices=PAY_CHOICES, max_length=15)
    order_comments = models.TextField(blank=True, null=True)
