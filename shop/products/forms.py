from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Product,Order

class ProductForm(forms.ModelForm):


    class Meta:
        model = Product
        fields = ['photo','name', 'description','price', 'category']

class OrdersForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = ['product', 'user', 'promo']

class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username','email','password1','password2']


class ReviewForm(forms.Form):
    text = forms.CharField(min_length=1, max_length=255)


class LoginForm(forms.Form):
    username = forms.CharField(min_length=4, max_length=30)
    password = forms.CharField(min_length=5, max_length=16)

class UserCodeForm(forms.Form):
    code = forms.IntegerField(max_value=9999, min_value=1000)
