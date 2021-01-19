from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

User = get_user_model()
#settings.AUTH_USER_MODEL

#*****************
#1 Category +
#2 Product +
#3 CartProduct +
#4 Cart +
#5 Order
#*****************
#6 Customer +
#7 Specification +

class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name="Назва категорії")
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    
    class Meta:
        abstract = True
    
    category = models.ForeignKey(Category, verbose_name="Категорія", on_delete=models.CASCADE)
    title = models.CharField(max_length=255, verbose_name="Назва товару")
    slug = models.SlugField(unique=True)
    image = models.ImageField(verbose_name="Зображення")
    description = models.TextField(verbose_name='Опис', null=True)
    price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name="Ціна")
    
    def __str__(self):
        return self.title


class CartProduct(models.Model):
    user = models.ForeignKey('Customer', verbose_name="Покупець", on_delete=models.CASCADE)
    cart = models.ForeignKey('Cart', verbose_name='Корзина', on_delete=models.CASCADE, related_name="related_products")
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    qty = models.PositiveIntegerField(default=1)
    final_price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name="Загальна ціна")
    
    def __str__(self):
        return "Продукт: {} (для корзини)".format(self.content_type.title)
    
class Cart(models.Model):
    owner = models.ForeignKey('Customer', verbose_name="Власник", on_delete=models.CASCADE)
    products = models.ManyToManyField(CartProduct, blank=True, related_name="related_cart")
    total_products = models.PositiveIntegerField(default=0)
    final_price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name="Загальна ціна")

    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)
        self.id = None

    def __str__(self):
        return str(self.id)
    
class Customer(models.Model):
    user = models.ForeignKey(User, verbose_name='Користувач', on_delete=models.CASCADE)
    phone = models.CharField(max_length=20, verbose_name="Номер телефону")
    address = models.CharField(max_length=255, verbose_name="Адрес")
    
    def __str__(self):
        return "Покупець: {} {}".format(self.user.first_name, self.user.last_name)
  
class NotebookProduct(Product):
    diagonal = models.CharField(max_length=255, verbose_name="Діагональ")

# https://www.youtube.com/watch?v=pEe894MhhVs

