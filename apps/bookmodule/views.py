from django.shortcuts import render
from django.http import HttpResponse

def index2(request, val1=0):
   return render(request, "bookmodule/index2.html", {"value": val1})

def viewbook(request, bookId):
    # assume that we have the following books somewhere (e.g. database)
    book1 = {'id':123, 'title':'Continuous Delivery', 'author':'J. Humble and D. Farley'}
    book2 = {'id':456, 'title':'Secrets of Reverse Engineering', 'author':'E. Eilam'}
    targetBook = None
    if book1['id'] == bookId: targetBook = book1
    if book2['id'] == bookId: targetBook = book2
    context = {'book':targetBook} # book is the variable name accessible by the template
    return render(request, 'bookmodule/show.html', context)

### Lab-4
def index(request):
    return render(request, "bookmodule/index.html")
 
def list_books(request):
    return render(request, 'bookmodule/list_books.html')
 
def viewbook(request, bookId):
    return render(request, 'bookmodule/one_book.html')
 
def about_us(request):
    return render(request, 'bookmodule/about_us.html')

### Lab-5
def lab5(request):
    return render(request, 'bookmodule/lab5.html')

# lab-3
#def index(request):
#    name = request.GET.get("name") or "world!"
#    return render(request, "bookmodule/index.html" , {"name": name})