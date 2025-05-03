from django import forms
from .models import Book10, Book11, BookWithCover, Author11

class BookForm(forms.ModelForm):
    class Meta:
        model = Book10
        fields = ['title', 'price', 'edition', 'author']

#lab 11
class Book11Form(forms.ModelForm):
    class Meta:
        model = Book11
        fields = ['title', 'price', 'edition', 'authors']
    
    title = forms.CharField(label="Title", required=True)
    price = forms.FloatField(label="Price (with decimal point)", required=True, initial=0.00)
    edition = forms.IntegerField(label="Edition", required=True, initial=1)
    authors = forms.ModelMultipleChoiceField(
        label="Authors",
        queryset=Author11.objects.all().order_by("fullname"),
        widget=forms.CheckboxSelectMultiple()
    )


class BookWithCoverForm(forms.ModelForm):
    class Meta:
        model = BookWithCover
        fields = ['title', 'price', 'edition', 'authors', 'cover_page']
    
    title = forms.CharField(label="Title", required=True)
    price = forms.FloatField(label="Price (with decimal point)", required=True, initial=0.00)
    edition = forms.IntegerField(label="Edition", required=True, initial=1)
    authors = forms.ModelMultipleChoiceField(
        label="Authors",
        queryset=Author11.objects.all().order_by("fullname"),
        widget=forms.CheckboxSelectMultiple()
    )
    cover_page = forms.ImageField(label="Book Cover", required=True)