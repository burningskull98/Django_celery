from django.core.management.base import BaseCommand
from shop_app.models import Category, Product


class Command(BaseCommand):
    help = 'Generate test data'

    def handle(self, *args, **options):

        category1 = Category.objects.create(name='pie', description='flour product')

        category2 = Category.objects.create(name='cake', description='flour product')

        category3 = Category.objects.create(name='bento-cake', description='flour product')

        category4 = Category.objects.create(name='pastry', description='flour product')

        Product.objects.create(name='potato cake',
                               description='ingredients: granulated sugar, wheat flour, '
                                           'vegetable cream (palm kernel oil, normalized cream, '
                                           'milk protein, carrageenan), egg, butter, margarine (vegetable oils, '
                                           'salt, milk whey, sugar),cocoa powder, sour cream, condensed milk with sugar,'
                                           ' table salt, baking powder, flavoring, sorbic acid.,'
                                           ' sugar syrup, butter, cocoa', price=300, quantity=6, category=category4)

        Product.objects.create(name='Sour cream with minced meat',
                               description='ingredients: flour, granulated sugar, egg, yeast, vegetable oil,'
                                           ' minced meat (pork, beef, chicken fillet), rice, onion, cheese, mayonnaise, '
                                           'sour cream, black pepper, salt, vanillin.,sugar syrup, butter, cocoa',
                               price=99, category=category1)

        Product.objects.create(name='Medovik',
                               description='ingredients: sour cream, wheat flour, condensed boiled milk, granulated sugar, '
                                           'vegetable cream (palm kernel oil, normalized cream,milk protein, carrageenan),'
                                           ' natural honey, egg,margarine(vegetable oils, salt, milk whey, sugar),'
                                           ' baking soda, vanilla glaze.', price=2000, category=category2)

        Product.objects.create(name='Vanilla with strawberries',
                               description='ingredients: egg, sugar, wheat flour, baking powder, corn starch, '
                                           'sunflower oil, vanilla, milk, strawberries, 82.5% butter, cottage cheese, '
                                           'powdered sugar, food coloring', price=1500, category=category3)

        self.stdout.write(self.style.SUCCESS('Тестовые записи успешно созданы!'))
