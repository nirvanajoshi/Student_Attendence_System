from django.contrib import admin
from .models import Attendance


@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = (
        "student",
        "subject",
        "date",
        "status",
        "marked_by",
    )

    list_filter = (
        "date",
        "status",
        "subject",
    )

    search_fields = (
        "student__student_id",
        "student__user__username",
        "subject__name",
        "subject__code",
        "marked_by__username",
    )

    ordering = ("-date",)