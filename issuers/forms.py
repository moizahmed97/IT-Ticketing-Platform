from django import forms 
from issues.models import Technician
from django.contrib.auth import get_user_model



User = get_user_model()

class TechnicianModelForm(forms.ModelForm):
    class Meta:
        model = User
        fields = (
            'email',
            'username',
            'first_name',
            'last_name',
        )