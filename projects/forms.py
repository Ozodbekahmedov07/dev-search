from django import forms
from .models import Project, Tags, Reviews

class ProjectForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={
        "class": "input input--text"
    }))
    description = forms.CharField(widget=forms.Textarea(attrs={
        "class": "input input--text"
    }))
    image = forms.ImageField(widget=forms.FileInput(attrs={
        "class": "input input--text"
    }), required=False)
    tags = forms.ModelMultipleChoiceField(queryset=Tags.objects.all(), widget=forms.CheckboxSelectMultiple(attrs={
        "class": "input input--text"
    }))
    source_link = forms.CharField(widget=forms.TextInput(attrs={
        "class": "input input--text"
    }))
    demo_link = forms.CharField(widget=forms.TextInput(attrs={
        "class": "input input--text"
    }))
    class Meta:
        model = Project
        fields = ('name', 'description', 'image', 'tags', 'source_link', 'demo_link')



class ReviewForm(forms.ModelForm):
    text = forms.CharField(widget=forms.Textarea(attrs={
        "class": "input input--text"
    }))

    class Meta:
        model = Reviews
        fields = ['text', 'body']