from django.contrib import admin

from .models import ShoppingCart, CartItem


# admin.site.register(ShoppingCart)
# admin.site.register(CartItem)


class CartItemInline(admin.TabularInline):
    model = CartItem
    raw_id_fields = ['product']


class ShoppingCartAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ShoppingCart._meta.fields]
    inlines = [CartItemInline]


admin.site.register(ShoppingCart, ShoppingCartAdmin)
