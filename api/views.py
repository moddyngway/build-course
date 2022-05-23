from django.shortcuts import render
from rest_framework.generics import ListAPIView

from api.serializers import ProjectSerializer, CheckSerializer
from blog.models import Blog
from projects.models import Project, Check


class ProjectListAPIView(ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class CheckListAPIView(ListAPIView):
    queryset = Check.objects.all()
    serializer_class = CheckSerializer


class BlogListAPIView(ListAPIView):
    queryset = Blog.objects.all()
    serializer_class = ProjectSerializer
