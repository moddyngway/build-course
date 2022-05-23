from django.urls import path
from . import views

urlpatterns = [
    path('projects/', views.ProjectListAPIView.as_view(), name='projects_api'),
    path('blogs/', views.BlogListAPIView.as_view(), name='blog_api'),
    path('checks/', views.CheckListAPIView.as_view(), name='check_api'),
]
