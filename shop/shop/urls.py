"""shop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from products.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',homepage, name= 'home'),
    path('category/', category_list, name='categories'),
    path('category/<str:category_name>/', category_products, name= 'category_products'),
    path('product_create/', product_post),
    path('my_orders/',my_orders, name= 'my_orders'),
    path('order_create/<str:product_name>/', order_create, name='order_create'),
    path('confirm_order/<int:order_id>/', confirm_order, name='confirm_order'),
    path('registration/', user_registr),
    path('product/<int:product_id>/',product_detail, name='product_detail'),
    path('product_update/<int:product_id>/', product_update, name= 'product_update'),
    path('product_delete/<int:product_id>/', delete_product, name= 'product_delete'),
    path('order_update/<int:order_id>/', order_update, name='order_update'),
    path('delete_order/<int:order_id>/', delete_order, name='delete_order'),

    ] + static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
