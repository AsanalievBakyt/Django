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
    quantity = models.IntegerField(default=10, verbose_name= 'Кол-во на скаладе')


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
