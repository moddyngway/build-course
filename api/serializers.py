from rest_framework import serializers

from blog.models import Blog
from projects.models import Project, Category, Check


class ProjectSerializer(serializers.ModelSerializer):

    category_str = serializers.SerializerMethodField()

    class Meta:
        model = Project
        fields = '__all__'

    def get_category_str(self, obj):
        res = []
        for cat in obj.categories.all():
            res.append(cat.title)
        return '-'.join(res)


class BlogSerializer(serializers.ModelSerializer):
    category_str = serializers.SerializerMethodField()

    class Meta:
        model = Blog
        fields = '__all__'

    def get_category_str(self, obj):
        res = []
        for cat in obj.categories.all():
            res.append(cat.title)
        return '-'.join(res)


class CheckSerializer(serializers.ModelSerializer):
    class Meta:
        model = Check
        fields = '__all__'
