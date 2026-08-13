from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.utils import timezone

from attendance.models import Attendance
from students.models import Student
from subjects.models import Subject


@login_required
def dashboard_view(request):
    """Calculates summary statistics and renders the main dashboard."""

    # Total counts
    total_students = Student.objects.count()
    total_subjects = Subject.objects.count()

    # Today's attendance
    today = timezone.localdate()
    today_attendance = Attendance.objects.filter(date=today)

    # Attendance status counts
    present_today = today_attendance.filter(status="present").count()
    absent_today = today_attendance.filter(status="absent").count()
    late_today = today_attendance.filter(status="late").count()

    # Attendance percentage
    total_today = today_attendance.count()

    attendance_percentage = (
        round((present_today / total_today) * 100, 1)
        if total_today > 0
        else 0
    )

    # Data sent to template
    context = {
        "total_students": total_students,
        "total_subjects": total_subjects,
        "present_today": present_today,
        "absent_today": absent_today,
        "late_today": late_today,
        "attendance_percentage": attendance_percentage,
    }

    return render(
        request,
        "dashboard/dashboard.html",
        context,
    )