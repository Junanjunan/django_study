from django.urls import path
from . import views


urlpatterns = [
    path('', views.home),
    path('ajax-test', views.ajax_data_view),
]