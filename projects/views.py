from django.shortcuts import render
from django.views.generic import ListView

from core.models import Rewards
from projects.models import Project, Category


class ProjectListView(ListView):
    template_name = 'projects.html'
    model = Project
    context_object_name = 'projects'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)

        context['categories'] = Category.objects.all()
        return context


class HomeTemplateView(ListView):
    template_name = 'index.html'
    model = Project
    context_object_name = 'projects'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)

        context['categories'] = Category.objects.all()
        context['rewards'] = Rewards.objects.all()

        return context
