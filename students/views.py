from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from .forms import StudentForm
from .models import Student

@login_required
def student_list(request):
    """Displays a list of all students."""
    students = Student.objects.all()
    return render(request, "students/student_list.html", {"students": students})

@login_required
def student_detail(request, pk):
    """Displays detailed information for a single student."""
    student = get_object_or_404(Student, pk=pk)
    return render(request, "students/student_detail.html", {"student": student})

@login_required
def student_create(request):
    """Handles adding a new student record."""
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            student = form.save(commit=False)
            student.user = request.user
            student.save()
            messages.success(request, "Student added successfully!")
            return redirect("students:student_detail", pk=student.pk)
    else:
        form = StudentForm()

    return render(request, "students/student_form.html", {"form": form, "title": "Add Student"})

@login_required
def student_edit(request, pk):
    """Handles updating an existing student record."""
    student = get_object_or_404(Student, pk=pk)

    if request.method == "POST":
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            messages.success(request, "Student updated successfully!")
            return redirect("students:student_detail", pk=student.pk)
    else:
        form = StudentForm(instance=student)

    return render(
        request,
        "students/student_form.html",
        {"form": form, "student": student, "title": "Edit Student"},
    )
    
    
@login_required
def student_delete(request, pk):
    """Handles deleting a student record."""
    student = get_object_or_404(Student, pk=pk)

    if request.method == "POST":
        student.delete()
        messages.success(request, "Student deleted successfully!")
        return redirect("students:student_list")

    return render(
        request, "students/student_confirm_delete.html", {"student": student}
    )