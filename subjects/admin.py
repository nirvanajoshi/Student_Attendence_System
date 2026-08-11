from django.contrib import admin
from .models import Subject


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ("name", "code", "teacher", "semester")
    list_filter = ("semester",)
    search_fields = (
        "name",
        "code",
        "teacher__username",
        "teacher__first_name",
        "teacher__last_name",
    )
    ordering = ("code",)