from django.contrib.auth.forms import UserCreationForm, forms
from App_login.models import CustomUser


class SignupForm(UserCreationForm):
    dob = forms.CharField(widget=forms.TextInput(attrs={'type': 'date'}))

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2', 'profile_picture', 'gender',
                  'phone_number', 'dob', 'address')

