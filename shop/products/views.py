from django.shortcuts import render, redirect
from .models import Product, Category, Order
from .forms import ProductForm, OrdersForm, RegisterForm
from django.http import HttpResponse


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
    return render(request,'my_orders.html', context={'orders': orders})

def order_create(request,product_name):
    product = Product.objects.get(name__iexact=product_name)
    form = OrdersForm(initial={'user': request.user,'product': product})
    if request.method == 'POST':
        form = OrdersForm(request.POST, initial={'user': request.user})
        if form.is_valid():
            form.save()
        return HttpResponse(f'Заказ оформлен')
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
    form = RegisterForm()
    if request.method =='POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse(f'Регистрация прошла успешно')
    return render(request,'registration.html', context={'form':form})

