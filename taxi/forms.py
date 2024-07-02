import re

from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.forms import ModelForm

from taxi.models import Driver


class DriverCreateForm(UserCreationForm):
    class Meta:
        model = Driver
        fields = UserCreationForm.Meta.fields + ("license_number",)

    def validate_license_number(self):
        breakpoint()
        license_number: str = self.cleaned_data["license_number"]
        pattern = re.compile(r"^[A-Z]{3}\d{5}$")

        if not re.match(pattern, license_number):
            raise ValidationError("Invalid license number format 1")


class DriverLicenseUpdateForm(ModelForm):
    class Meta:
        model = Driver
        fields = ("license_number",)

    def clean_license_number(self):
        license_number: str = self.cleaned_data["license_number"]
        pattern = re.compile(r"^[A-Z]{3}\d{5}$")

        if not re.match(pattern, license_number):
            raise ValidationError("Invalid license number format 2")