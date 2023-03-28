from django.urls import path
from . import views
import os
from django.http import HttpResponse, HttpResponseNotFound, FileResponse
import uuid




urlpatterns = [
    path('', views.home),
    path('crawl', views.crawl_reallinux),
    path('video', views.stream_video),
    path('stream', views.token_video),
    path('video_test', views.video_test),
]

