from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

# This form extends the default UserCreationForm to include additional fields for user signup.
class SignupForm(UserCreationForm):
    name = forms.CharField(max_length=255, required=True)
    image = forms.ImageField(required=False)

    class Meta:
        model = CustomUser
        fields = ['username', 'name', 'image', 'password1', 'password2']
