from django import forms
from django.contrib.auth.forms import UserCreationForm
from userauths.models import User, GENDER


class UserRegisterForm(UserCreationForm):
    full_name = forms.CharField(widget=forms.TextInput(attrs={'class': '', 'id': "", 'placeholder':'Full Name'}), max_length=100, required=True)
    username = forms.CharField(widget=forms.TextInput(attrs={'class': '', 'id': "", 'placeholder':'Username'}), max_length=100, required=True)
    phone = forms.CharField(widget=forms.TextInput(attrs={'class': '', 'id': "", 'placeholder':'Mobile No.'}), max_length=100, required=True)
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': '' , 'id': "", 'placeholder':'Email Address'}), required=True)
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'id': "", 'placeholder':'Password'}), required=True)
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'id': "", 'placeholder':'Confirm Password'}), required=True)
    gender = forms.ChoiceField(choices=GENDER, widget=forms.Select(attrs={'class': 'selectpicker mt-2 with-border', 'placeholder': 'Gender'}))

    class Meta:
        model = User
        fields = ['full_name', 'username', 'email', 'password1', 'password2', 'phone', 'gender']


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'with-border'


