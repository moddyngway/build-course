from django.shortcuts import render
from django.views.generic import ListView, DetailView

from blog.models import Blog, Category


class BlogListView(ListView):
    model = Blog
    template_name = 'blog.html'
    context_object_name = 'blogs'

    def get_queryset(self):
        focus = self.request.GET.get('s')
        category = self.request.GET.get('cat')

        if focus:
            return Blog.objects.filter(title__contains=focus)
        elif category:
            return Blog.objects.filter(categories__code=category)
        else:
            return Blog.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)

        context['categories'] = Category.objects.all()
        return context


class BlogDetailView(DetailView):
    model = Blog
    template_name = 'blog-single.html'
    context_object_name = 'blog'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)

        context['blogs'] = Blog.objects.all()
        return context
