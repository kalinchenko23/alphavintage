from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home),
    path('cryptocurrency/',views.crypto),
    path('exchange/',views.exchange_rate),
    path('cp_search/',views.cp_search),
    path('company_info/',views.data),
    path('stock_info/',views.stock),
    path('stock_history/',views.stock_history),
    path('sector/',views.sector)
    ]