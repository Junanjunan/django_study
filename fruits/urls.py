from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('fruit', views.fruit_view),
    path('fruit2', views.fruit_view2),
    path('fruit3', views.fruit_view3),
    path('fruit4', views.fruit_view4),

    path('shop', views.shopw_view),

    path('intersection', views.intersection_view),
]