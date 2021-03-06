import random

from django.contrib.auth import authenticate, login
from django.core.mail import EmailMessage
from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.http import HttpResponse
from .services import use_promo
from django.utils import timezone



def homepage(request):
    if 'search' in request.GET:
        condition = request.GET['search']
        ps = Product.objects.filter(name__icontains = condition)
    else:
        ps = Product.objects.all()
    return render(request,'homepage.html', context={'ps': ps})

def category_list(request):
    categories = Category.objects.all()
    return render(request, 'categories.html', context={'cats': categories})


def category_products(request, category_name):
    products = Product.objects.filter(category__name=category_name)
    return render(request,'homepage.html', context={'ps': products})

def product_post(request):
    form = ProductForm()
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse(f'Car created successfully')
    return render(request,'create_product.html', context={'form': form})

def my_orders(request):
    orders = Order.objects.filter(user=request.user)
    now = timezone.now()
    aval = timezone.timedelta(minutes=10)
    return render(request,'my_orders.html', context={'orders': orders,
                                                     'now': now,
                                                     'aval':aval})

def order_create(request,product_name):
    product = Product.objects.get(name__iexact=product_name)
    form = OrdersForm(initial={'user': request.user,'product': product})
    if request.method == 'POST':
        form = OrdersForm(request.POST, initial={'user': request.user})
        if form.is_valid():
            price = form.instance.product.price
            promo = form.cleaned_data.get('promo')
            if promo:
                total = use_promo(promo,price)
            else:
                total = price
            form.instance.total = total
            form.save()
        return HttpResponse(f'?????????? ????????????????')
    return render(request, 'order_create.html', context={'form': form})

def confirm_order(request, order_id):
    order = Order.objects.get(id=order_id)
    if request.method == 'POST':
        order.status = 'closed'
        order.product.quantity -= 1
        order.product.save()
        order.save()
        return redirect('my_orders')
    return render(request, 'confirm_order.html')

def user_registr(request):
    import random
    form = RegisterForm()
    if request.method =='POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.instance.is_active = False
            form.save()
            code = random.randint(1000,9999)
            UserCode.objects.create(user=form.instance, code=code)
            recipient = form.cleaned_data.get('email')
            subject = 'New User'
            body = f'Welcome to our site! Your registration code is {code}'
            e = EmailMessage(subject=subject, body=body,to=[recipient,])
            e.send()
            return HttpResponse(f'?????????????????????? ???????????? ??????????????')
    return render(request,'registration.html', context={'form':form})

def product_detail(request, product_id):
    product = Product.objects.get(id=product_id)
    o = Order.objects.filter(product=product, status='closed')
    form = ReviewForm()
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data.get('text')
            Review.objects.create(user=request.user, product=product, text=text)
    return render(request, 'product_detail.html',context={'p': product,
                                                          'form': form,
                                                          'o': o})

def product_update(request, product_id):
    product = Product.objects.get(id=product_id)
    form = ProductForm(instance=product)
    if request.method == 'POST':
        form = ProductForm(request.POST,request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_detail', product_id)
    return render(request,'create_product.html', context={'form': form})

def delete_product(request, product_id):
    product = Product.objects.get(id=product_id)
    if request.method == 'POST':
        product.delete()
        return redirect('home')
    return render(request, 'product_delete.html', context={'p': product})

def order_update(request, order_id):
    order = Order.objects.get(id=order_id)
    form = OrdersForm(instance=order)
    if request.method == 'POST':
        now = timezone.now()
        aval = timezone.timedelta(minutes=10)
        diff = now - order.date
        if diff <= aval:
            form = OrdersForm(request.POST, instance=order)
            if form.is_valid():
                form.save()
                return redirect('my_orders')
        else:
            return HttpResponse(f'?????????? ??????????????')
    return render(request,'order_create.html', context={'form': form})

def delete_order(request, order_id):
    order = Order.objects.get(id=order_id)
    if request.method == 'POST':
        order.delete()
        return redirect('my_orders')
    return render(request, 'delete_order.html', context={'o': order})

def login_page(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            l = User.objects.get(username=username)
            login(request,user)
            if not l.is_active:
                return redirect('user_activate',username)
            return redirect('home')
    return render(request,'login_page.html',{'form':form})

def activate_user(request,username):
    user = User.objects.get(username=username)
    form = UserCodeForm()
    if request.method == 'POST':
        form = UserCodeForm(request.POST)
        if form.is_valid():
            code = form.cleaned_data.get('code')
            user_code = UserCode.objects.filter(user=user, code=code)
            if user_code:
                user.is_active = True
                user.save()
                return redirect('login_user')
    return render(request,'activate_user.html',context={'form':form})