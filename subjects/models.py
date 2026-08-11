from django.db import models
from django.contrib.auth.models import User


class Subject(models.Model):
    SEMESTER_CHOICES = (
        (1, "Semester 1"),
        (2, "Semester 2"),
        (3, "Semester 3"),
        (4, "Semester 4"),
        (5, "Semester 5"),
        (6, "Semester 6"),
        (7, "Semester 7"),
        (8, "Semester 8"),
    )

    name = models.CharField(max_length=100)
    code = models.CharField(max_length=20, unique=True)
    description = models.TextField(blank=True)

    teacher = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name="subjects")
    semester = models.PositiveSmallIntegerField(choices=SEMESTER_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.code} - {self.name}"