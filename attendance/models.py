from django.db import models
from django.contrib.auth.models import User
from apps.subjects.models import Subject
from apps.students.models import Student


class Attendance(models.Model):
    STATUS_CHOICES = (
        ("present", "Present"),
        ("absent", "Absent"),
        ("late", "Late"),
    )

    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="attendances")

    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name="attendances")

    date = models.DateField()

    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="present")

    marked_by = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True, related_name="marked_attendances"
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["student", "subject", "date"],
                name="unique_student_subject_date_attendance",
            )
        ]

    def __str__(self):
        return (
            f"{self.student} - {self.subject.code} "
            f"({self.date}): {self.get_status_display()}"
        )