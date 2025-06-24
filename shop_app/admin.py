from django.contrib import admin
from .models import Product, Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']
    search_fields = ['name', 'description']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price', 'quantity', 'category', 'created_at')
    ordering = ('category', 'created_at',)
    list_filter = ('name', 'price')
    search_fields = ('name', 'description')
    search_help_text = 'Поиск по названию и составу'

    @admin.action(description='Изменить цену')
    def change_price(self, request, queryset):
        for product in queryset:
            product.price += 100
            product.price -= 100
            product.save()
        self.message_user(request, 'Цена успешно изменилась')

    @admin.action(description='Опубликовать выбранный товар')

    def publish_product(self, request, queryset):
        queryset.update(is_published=True)
        self.message_user(request, "Выбранные товары успешно опубликованы.")


actions = ['change_price', 'publish_product']
