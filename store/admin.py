from django.contrib import admin

from store.models import Product, Category, Subcategory, Cart, CartItem


# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'price', 'subcategory',)
    list_filter = ('title', 'slug', 'price',)
    search_fields = ('title', 'slug', 'price',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug',)
    list_filter = ('title', 'slug',)
    search_fields = ('title',)


@admin.register(Subcategory)
class SubcategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'category',)
    list_filter = ('title', 'slug', 'category',)
    search_fields = ('title',)


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('user', 'created_at',)
    list_filter = ('user',)


@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ('cart', 'product', 'quantity',)
    list_filter = ('cart', 'product', 'quantity',)
    search_fields = ('cart', 'product', 'quantity',)
