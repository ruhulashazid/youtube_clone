from django import forms
from django.contrib.auth.forms import UserCreationForm
from userauths.models import User 

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(widget=forms.TextInput(attrs={'class':'validate', 'id':'reg_user_name'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'', 'id':'reg_pass_word', 'onkeyup': 'validate()'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'', 'id':'re_pass_word', 'onkeyup': 'validate()'}))

    class Meta:
        model = User
        fields = [
            'username', 
            'email', 
            'first_name', 
            'last_name', 
            'password1', 
            'password2'
            ]