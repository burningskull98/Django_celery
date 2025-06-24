import pytest
from shop_app.models import Product, Category


@pytest.mark.django_db
def test_create_product():
    category = Category.objects.create(name='Тестовое название', description='Тестовое описание')
    product = Product.objects.create(name='Тест название продукта', description='Новое описание', price=400,
                                     category=category)

    assert product.name == 'Тест название продукта'
    assert product.price == 400
    assert product.category == category


@pytest.mark.django_db
def test_update_product():
    category = Category.objects.create(name='Название для тест', description='Описание теста')
    product = Product.objects.create(name='Тест меняет название', description='Тестовое изменение', price=730,
                                     category=category)

    product.price = 500
    product.save()

    assert product.price == 500


@pytest.mark.django_db
def test_delete_product():
    category = Category.objects.create(name='Категория для теста', description='Описание для теста')
    product = Product.objects.create(name='Продукт для удаления', description='Последний рубеж', price=461,
                                     category=category)

    assert Product.objects.filter(id=product.pk).exists()

    product.delete()

    assert not Product.objects.filter(id=product.pk).exists()


@pytest.mark.django_db
def test_read_product():
    category = Category.objects.create(name='Категория для чтения', description='Оп чтения теста')

    product1 = Product.objects.create(name='Продукт для чтения1', description='Опись', price=914, category=category)
    product2 = Product.objects.create(name='Продукт для чтения2', description='2-й продукт', price=1018,
                                      category=category)

    assert Product.objects.count() == 2

    retrieved_product1 = Product.objects.get(id=product1.pk)
    assert retrieved_product1.name == 'Продукт для чтения1'
    assert retrieved_product1.price == 914

    retrieved_product2 = Product.objects.get(id=product2.pk)
    assert retrieved_product2.name == 'Продукт для чтения2'
    assert retrieved_product2.price == 1018

    assert retrieved_product1.description == 'Опись'
    assert retrieved_product2.description == '2-й продукт'
