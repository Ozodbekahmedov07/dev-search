from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from django.contrib.auth import password_validation
from django.utils.translation import gettext_lazy as _
from .models import Profile, Skills, Inbox


class UserRegisterForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'input input--text'
    }))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'input input--text'
    }))
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'input input--text'
    }))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'class': 'input input--email'
    }))
    password1 = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password", 'class': 'input input--password'}),
        help_text=password_validation.password_validators_help_text_html(),
    )
    password2 = forms.CharField(
        label=_("Password confirmation"),
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password", 'class': 'input input--password'}),
        strip=False,
        help_text=_("Enter the same password as before, for verification."),
    )

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username', 'password1', 'password2')


class ProfileForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'input input--text'
    }))
    name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'input input--text'
    }))
    location = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'input input--text',
        'required': 'False'
    }), required=False)
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'class': 'input input--email',
        'required': 'False'
    }), required=False)
    short_intro = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'input input--text',
        'required': 'False'
    }), required=False)
    bio = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'input input--text',
        'required': 'False'
    }), required=False)
    image = forms.ImageField(widget=forms.FileInput(attrs={
        'class': 'input input--text',
        'required': 'False'
    }), required=False)
    social_github = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'input input--email',
        'required': 'False'
    }), required=False)
    social_linkedin = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'input input--email',
        'required': 'False'
    }), required=False)
    social_stackoverflow = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'input input--email',
        'required': 'False'
    }), required=False)
    social_twitter = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'input input--email',
        'required': 'False'
    }), required=False)
    social_website = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'input input--email',
        'required': 'False'
    }), required=False)
    social_telegram = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'input input--email',
        'required': 'False'
    }), required=False)
    social_instagram = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'input input--email',
        'required': 'False'
    }), required=False)

    class Meta:
        model = Profile
        fields = '__all__'


class SkillsForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'input input--text'
    }))
    description = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'input input--text'
    }))

    class Meta:
        model = Skills
        fields = ('name', 'description')


class MeesageForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'input input--text',
        'placeholder': 'Name'
    }))
    subject = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'input input--text',
        'placeholder': 'Subject'
    }))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'class': 'input input--email',
        'required': 'False',
        'placeholder': 'Email'
    }), required=False)

    body = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'input input--text',
        'placeholder': 'Your message'
    }))

    class Meta:
        model = Inbox
        fields = ['name', 'email', 'subject', 'body']
