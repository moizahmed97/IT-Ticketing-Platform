from django import forms 
from issues.models import Issuer
from django.contrib.auth import get_user_model



User = get_user_model()

class IssuerModelForm(forms.ModelForm):
    class Meta:
        model = User
        fields = (
            'email',
            'username',
            'first_name',
            'last_name',
        )