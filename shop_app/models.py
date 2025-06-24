from django.db import models


class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=150, verbose_name='Название категории', default='', null=True)
    description = models.TextField(blank=True, verbose_name='Описание',)

    def __str__(self):
        return self.name



class Product(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название товара', null=True)
    description = models.TextField(blank=True, verbose_name='Состав')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    quantity = models.IntegerField(blank=True, default=0, verbose_name='Количество')
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')


def __str__(self):
    return self.name



