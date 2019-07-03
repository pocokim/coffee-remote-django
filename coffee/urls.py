# -*- coding: utf-8 -*-
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from shop import views
from order import views as order_views

router = DefaultRouter()
router.register(r'menu', views.MenuViewSet)
router.register(r'shoppinglist', order_views.OrderViewSet)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('rest-auth/kakao/', order_views.KakaoLogin.as_view(), name='kakao_login'),
]
