from django.contrib import admin
from .models import Category, Product, Order, OrderItem, Review
# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Category, CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['product_name', 'price', 'stock', 'hot_deals', 'featured_products', 'product_created_at', 'product_updated_at']
    list_editable = ['price', 'stock']
    prepopulated_fields = {'slug': ('product_name',)}
    list_per_page = 20


admin.site.register(Product, ProductAdmin)
# admin.site.register(Brand)
# admin.site.register(Color)
# admin.site.register(Available)


class OrderItemAdmin(admin.TabularInline):
    model = OrderItem
    fieldsets = [
        ('Product', {'fields': ['product'], }),
        ('Quantity', {'fields': ['quantity'], }),
        ('Price', {'fields': ['price'], }),
    ]
    readonly_fields = ['product', 'quantity', 'price']
    can_delete = False
    max_num = 0


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'billingName', 'emailAddress', 'created']
    list_display_links = ('id', 'billingName')
    search_fields = ['id', 'billingName', 'emailAddress']
    readonly_fields = ['id', 'token', 'total', 'emailAddress', 'created',
                       'billingName', 'billingAddress1', 'billingCity', 'billingPostcode',
                       'billingCountry', 'shippingName', 'shippingAddress1', 'shippingCity',
                       'shippingPostcode', 'shippingCountry']

    fieldsets = [
        ('ORDER INFORMATION', {'fields': ['id', 'token', 'total', 'created']}),
        ('BILLING INFORMATION', {'fields': ['billingName', 'billingAddress1',
                                            'billingCity', 'billingPostcode', 'billingCountry', 'emailAddress']}),
        ('SHIPPING INFORMATION', {'fields': ['shippingName', 'shippingAddress1',
                                             'shippingCity', 'shippingPostcode', 'shippingCountry']}),
    ]

    inlines = [
        OrderItemAdmin,
    ]

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request):
        return False

admin.site.register(Review)
