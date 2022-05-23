from django.urls import path, include, reverse_lazy
from django.utils.functional import lazy
from django.views.generic import TemplateView, ListView, DetailView, CreateView

from blog.views import BlogListView, BlogDetailView
from core.models import Employee, Feedback
from projects.models import Project
from projects.views import ProjectListView, HomeTemplateView

urlpatterns = [


    path('contact-us/', CreateView.as_view(template_name='contact-us.html',
                                           model=Feedback,
                                           fields=['author', 'email', 'subject', 'text'],
                                           success_url=reverse_lazy('home'))
         , name='contacts'),

    path('shops/', TemplateView.as_view(template_name='shop.html'), name='shop'),
    path('shop/1/', TemplateView.as_view(template_name='shop-single.html'), name='shop-item'),
    path('shop/cart/', TemplateView.as_view(template_name='shop-cart.html'), name='cart'),

    path('', HomeTemplateView.as_view(), name='home'),

    path('projects/<int:pk>/', DetailView.as_view(
        template_name='projects-single.html',
        model=Project,
        context_object_name='project'
    ), name='project-single'),

    path('projects/', ProjectListView.as_view(), name='projects'),

    path('about-us/', ListView.as_view(template_name='about.html',
                                       model=Employee,
                                       context_object_name='employees'),
         name='about-us'),

    path('blogs/', BlogListView.as_view(), name='blog'),
    path('blogs/<int:pk>/', BlogDetailView.as_view(), name='blog-single'),
]
