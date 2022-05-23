from django.contrib import admin
from . import models


class ImagesInline(admin.TabularInline):
    model = models.ProjectImages


class ProjectAdmin(admin.ModelAdmin):
    inlines = [ImagesInline]


admin.site.register(models.Category)
admin.site.register(models.Check)
admin.site.register(models.Project, ProjectAdmin)
