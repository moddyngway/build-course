from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

from dashboard import views

urlpatterns = [
    path('', views.chart, name='dashboard'),
]