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

]

