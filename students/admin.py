from django.contrib import admin
from .models import Student


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("user", "student_id", "semester", "created_at")
    list_filter = ("semester", "gender")
    search_fields = (
        "student_id",
        "user__username",
        "user__email",
        "user__first_name",
        "user__last_name",
    )
    ordering = ("student_id",)