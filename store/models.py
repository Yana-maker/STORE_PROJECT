from django.db import models

from users.models import User

# Create your models here.
NULLABLE = {'null': True, 'blank': True}


class Category(models.Model):
    """модель категории"""

    title = models.CharField(max_length=50, verbose_name='название категории')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='slug имя')
    image = models.ImageField(upload_to='category/', verbose_name='изображение', **NULLABLE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'


class Subcategory(models.Model):
    """модель подкатегории"""

    title = models.CharField(max_length=50, verbose_name='название подкатегории')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='slug имя')
    image = models.ImageField(upload_to='subcategory/', verbose_name='изображение', **NULLABLE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='название категории')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'подкатегория'
        verbose_name_plural = 'подкатегории'


class Product(models.Model):
    """модель продукта"""

    title = models.CharField(max_length=50, verbose_name='название продукта')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='slug имя')
    image = models.ImageField(upload_to='product/', verbose_name='изображение', **NULLABLE)
    price = models.PositiveIntegerField(verbose_name='цена', default=100)
    subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE, verbose_name='название подкатегории')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'


class Cart(models.Model):
    """модель корзины"""

    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='пользователь')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Корзина пользователя - {self.user}'

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'


class CartItem(models.Model):
    """модель корзины с прдуктами """
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, verbose_name='корзина')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='продукты', related_name='product')
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.cart

    class Meta:
        verbose_name = 'Продукт в корзине'
        verbose_name_plural = 'Продукты в корзине'
