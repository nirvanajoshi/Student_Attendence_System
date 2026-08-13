from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from .forms import AttendanceForm
from .models import Attendance


@login_required
def attendance_list(request):
    """Displays a list of all attendance records, newest first."""
    attendances = Attendance.objects.all().order_by("-date")
    return render(
        request,
        "attendance/attendance_list.html",
        {"attendances": attendances},
    )


@login_required
def attendance_detail(request, pk):
    """Displays details for a specific attendance record."""
    attendance = get_object_or_404(Attendance, pk=pk)
    return render(
        request,
        "attendance/attendance_detail.html",
        {"attendance": attendance},
    )


@login_required
def attendance_create(request):
    """Handles marking a new attendance record."""
    if request.method == "POST":
        form = AttendanceForm(request.POST)
        if form.is_valid():
            attendance = form.save()
            messages.success(request, "Attendance marked successfully!")
            return redirect("attendance:attendance_detail", pk=attendance.pk)
    else:
        form = AttendanceForm()

    return render(
        request,
        "attendance/attendance_form.html",
        {"form": form, "title": "Mark Attendance"},
    )