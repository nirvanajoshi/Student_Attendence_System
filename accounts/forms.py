from django import forms
from .models import Profile


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["role", "phone", "profile_picture"]

        widgets = {
            "role": forms.Select(
                attrs={"class": "form-control"}
            ),
            "phone": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter phone number",
                }
            ),
            "profile_picture": forms.ClearableFileInput(
                attrs={"class": "form-control"}
            ),
        }