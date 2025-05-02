from django.urls import path
from .import views

urlpatterns = [
    #lab 3
    path('', views.index),
    path('index2/<int:val1>/', views.index2),
    path('<int:bookId>', views.viewbook),
    #lab 4
    path('', views.index, name= "books.index"),
    path('list_books/', views.list_books, name= "books.list_books"),
    path('<int:bookId>/', views.viewbook, name="books.view_one_book"),
    path('about_us/', views.about_us, name="books.about_us"),
    #lab 5
    path('lab5/', views.lab5, name='books.lab5'),
    #lab 6
    path('search/', views.search, name='books.search'),
    path('filterbooks/', views.filterbooks, name='books.filterbooks'),
    # lab 7
    path('simple/query', views.simple_query, name='simple_query'),
    path('complex/query', views.complex_query, name='complex_query'),
    #lab 8
    path('lab8', views.models_lab8, name='lab8'),  
    #lab 9 
    path('lab9', views.models_lab9, name='lab9'),
    #lab 10 -1
    path('lab10/listbooks', views.list_books, name='list_books'),
    path('books/lab10/addbook', views.add_book, name='add_book'),
    path('books/lab10/editbook/<int:id>', views.edit_book, name='edit_book'),
    path('books/lab10/deletebook/<int:id>', views.delete_book, name='delete_book'),
    #lab 10 -2 
    path('lab10/form/listbooks', views.list_books_form, name='list_books_form'),
    path('lab10/form/addbook', views.add_book_form, name='add_book_form'),
    path('lab10/form/editbook/<int:id>', views.edit_book_form, name='edit_book_form'),
    path('lab10/form/deletebook/<int:id>', views.delete_book_form, name='delete_book_form'),

]

