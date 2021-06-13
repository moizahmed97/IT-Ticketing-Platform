from issues.models import Technician
from django import forms 
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm,UsernameField

User = get_user_model()

# For the Signup view we are using our own User Creation Form
# The User model has a lot of fields but we are using only a few of them
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User 
        # The next two lines have come from the UserCreationForm (So take them as is)
        fields = ("username",)
        field_classes = {'username': UsernameField}

class AssignTechForm(forms.Form):
    technician = forms.ModelChoiceField(queryset=Technician.objects.all())