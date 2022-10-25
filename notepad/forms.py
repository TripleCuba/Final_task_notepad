from django.forms.models import ModelForm
from .models import Note, User, Category
from django import forms

from django.contrib.auth.forms import UserCreationForm


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'email']


class AddNoteForm(ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'note_text', 'note_image', 'category']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'note_text': forms.Textarea(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-select'}),
            'note_image': forms.FileInput(attrs={'class': 'form-control'})

        }


class UpdateNoteForm(ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'note_text', 'note_image', 'category']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'note_text': forms.Textarea(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-select'}),
            'note_image': forms.FileInput(attrs={'class': 'form-control'})

        }


class AddCategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ['category_title', 'description', 'category_image', 'user']
        widgets = {
            'category_title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'category_image': forms.FileInput(attrs={'class': 'form-control'})
        }


class UpdateCategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ['category_title', 'description', 'category_image']
        widgets = {
            'category_title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'category_image': forms.FileInput(attrs={'class': 'form-control'})}

class TotalNotesUpdateForm(ModelForm):
    class Meta:
        model = User
        fields = ['total_notes']


