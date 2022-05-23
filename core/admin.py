from django.contrib import admin

from core.models import Rewards, Employee, Feedback


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ("name", "role", "salary")
    list_filter = ("role", "salary")
    search_fields = ("name__startswith",)


admin.site.register(Rewards)
admin.site.register(Feedback)
