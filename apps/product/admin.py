from django.contrib import admin

from apps.product.models import Product, ProductImage


# admin.site.register(Product)
# admin.site.register(ProductImage)

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    raw_id_fields = ['product']


class ProductAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Product._meta.fields]
    inlines = [ProductImageInline]


admin.site.register(Product, ProductAdmin)
admin.site.register(ProductImage)

