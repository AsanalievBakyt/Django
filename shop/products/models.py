from django.contrib.auth.models import User
from django.db import models
from django.core import validators

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Product(models.Model):
    name = models.CharField(max_length=30, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    price = models.IntegerField(validators=[validators.MaxValueValidator(400000), validators.MinValueValidator(1000)],verbose_name='цена')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null= True, verbose_name='Категория')
    quantity = models.IntegerField(validators=[validators.MinValueValidator(0)], default=10, verbose_name= 'Кол-во на скаладе')
    photo = models.ImageField(default='car_default.jpeg')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ['name']

class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, verbose_name='Товар')
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, verbose_name='Пользователь')
    status = models.CharField(choices=(
        ('in_process', 'in_process'),
        ('ready','ready'),
        ('closed', 'closed')
),max_length = 20, default='in_process'
    )
    date = models.DateTimeField(auto_now_add=True)
    promo = models.CharField(max_length=6, validators=[validators.MinLengthValidator(6)], null=True, blank=True)
    total = models.IntegerField(default=0)
    date_updated = models.DateTimeField(auto_now=True, blank=True,null=True)

class Promo(models.Model):
    code = models.CharField(max_length=6, validators=[validators.MinLengthValidator(6)], unique=True)
    status = models.CharField(choices=(
        ('active', 'active'),
        ('dead', 'dead')
    ),max_length=20, default='active')
    sale = models.PositiveIntegerField(validators=[validators.MaxValueValidator(50)], default=10)

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    text = models.CharField(max_length=255, validators=[validators.MaxLengthValidator(1)])
    date_created = models.DateTimeField(auto_now_add=True)

class UserCode(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    code = models.IntegerField(validators=[validators.MinValueValidator(1000),validators.MaxValueValidator(9999)])
