"""purchases URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from orders import views
from orders.views import ProductsViewSet, UserView
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

r = DefaultRouter()
r.register('product', ProductsViewSet, basename="product")

urlpatterns = [
    path('register/', views.RegisterAccountView.as_view(), name='register'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('products/shop/<int:shop_id>/', views.ProductsByShop.as_view(), name='products_by_shop'),
    path('shops/', views.ShopView.as_view(), name='shops'),
    path('orders/<int:pk>/', views.StatusOrderView.as_view(), name='order_status'),
    path('basket/', views.BasketView.as_view(), name='basket'),
    path('accounts/', include('allauth.urls')),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/doc/', SpectacularSwaggerView.as_view(url_name='schema'), name='doc'),
    path('users/', UserView.as_view(), name='user-list')
] + r.urls
