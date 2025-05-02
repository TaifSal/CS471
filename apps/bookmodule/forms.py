from django import forms
from .models import Book10

class BookForm(forms.ModelForm):
    class Meta:
        model = Book10
        fields = ['title', 'price', 'edition', 'author']
