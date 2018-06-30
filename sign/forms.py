from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class SignUp(forms.Form):
    username = forms.CharField(label = "Username", min_length = 6, max_length = 24)
    email = forms.EmailField(label = "Email")
    password = forms.CharField(label = "Enter Password", widget = forms.PasswordInput)
    conf_password = forms.CharField(label = "Confirm Password", widget = forms.PasswordInput)
    first_name = forms.CharField(label = "First Name", required = False)
    last_name = forms.CharField(label = "Last Name", required = False)

    def clean_username(self):
        username = self.cleaned_data['username']
        r = User.objects.filter(username = username)

        if r.count():
            raise ValidationError('Username already exists.')

        return username

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        r = User.objects.filter(email = email)

        if r.count():
            raise ValidationError("Email already exists.")

        return email

    def clean_conf_password(self):
        password = self.cleaned_data['password']
        conf_password = self.cleaned_data['conf_password']

        if password != conf_password:
            raise ValidationError("Entered passwords do not match.")

        return conf_password

    def clean_first_name(self):
        return self.cleaned_data['first_name']

    def clean_last_name(self):
        return self.cleaned_data['last_name']

    def save(self, commit = True):
        user = User.objects.create_user(
                self.cleaned_data['username'],
                self.cleaned_data['email'],
                self.cleaned_data['password'],
                first_name = self.cleaned_data['first_name'],
                last_name = self.cleaned_data['last_name']
            )

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password', 'conf_password']

class Login(forms.Form):
    username = forms.CharField(label = "Username")
    password = forms.CharField(label = "Password " , widget = forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password']
