from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from .forms import SubjectForm
from .models import Subject


@login_required
def subject_list(request):
    """Displays a list of all subjects."""
    subjects = Subject.objects.all()

    return render(
        request,
        "subjects/subject_list.html",
        {"subjects": subjects},
    )


@login_required
def subject_detail(request, pk):
    """Displays detailed information for a single subject."""
    subject = get_object_or_404(Subject, pk=pk)

    return render(
        request,
        "subjects/subject_detail.html",
        {"subject": subject},
    )


@login_required
def subject_create(request):
    """Handles adding a new subject."""
    if request.method == "POST":
        form = SubjectForm(request.POST)

        if form.is_valid():
            subject = form.save()

            messages.success(
                request,
                "Subject created successfully!",
            )

            return redirect(
                "subjects:subject_detail",
                pk=subject.pk,
            )

    else:
        form = SubjectForm()

    return render(
        request,
        "subjects/subject_form.html",
        {
            "form": form,
            "title": "Add Subject",
        },
    )
@login_required
def subject_edit(request, pk):
    """Handles updating an existing subject."""
    subject = get_object_or_404(Subject, pk=pk)

    if request.method == "POST":
        form = SubjectForm(request.POST, instance=subject)

        if form.is_valid():
            form.save()
            messages.success(request, "Subject updated successfully!")
            return redirect(
                "subjects:subject_detail",
                pk=subject.pk,
            )
    else:
        form = SubjectForm(instance=subject)

    return render(
        request,
        "subjects/subject_form.html",
        {
            "form": form,
            "subject": subject,
            "title": "Edit Subject",
        },
    )


@login_required
def subject_delete(request, pk):
    """Handles deleting a subject."""
    subject = get_object_or_404(Subject, pk=pk)

    if request.method == "POST":
        subject.delete()
        messages.success(request, "Subject deleted successfully!")
        return redirect("subjects:subject_list")

    return render(
        request,
        "subjects/subject_confirm_delete.html",
        {"subject": subject},
    )