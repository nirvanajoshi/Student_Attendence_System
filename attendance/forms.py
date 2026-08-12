from django import forms
from .models import Attendance


class AttendanceForm(forms.ModelForm):
    class Meta:
        model = Attendance
        fields = ["student", "subject", "date", "status"]

        widgets = {
            "student": forms.Select(
                attrs={"class": "form-control"}
            ),
            "subject": forms.Select(
                attrs={"class": "form-control"}
            ),
            "date": forms.DateInput(
                attrs={
                    "class": "form-control",
                    "type": "date",
                }
            ),
            "status": forms.Select(
                attrs={"class": "form-control"}
            ),
        }