from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.db.models import Q, Count, Sum, Avg, Max, Min
# from .models import Book, Book9, Book10, Author, Publisher 
from .models import Book10, Book11, Author11, BookWithCover
from .forms import BookForm, Book11Form, BookWithCoverForm
from django.contrib.auth.decorators import login_required


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


# lab-3
#def index(request):
#    name = request.GET.get("name") or "world!"
#    return render(request, "bookmodule/index.html" , {"name": name})


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

### lab-6
def search(request):
    return render(request, 'bookmodule/search.html')

def __getBooksList():
    book1 = {'id':12344321, 'title':'Continuous Delivery', 'author':'J.Humble and D. Farley'}
    book2 = {'id':56788765,'title':'Reversing: Secrets of Reverse Engineering', 'author':'E. Eilam'}
    book3 = {'id':43211234, 'title':'The Hundred-Page Machine Learning Book', 'author':'Andriy Burkov'}
    return [book1, book2, book3]

def filterbooks(request):
    if request.method == "POST":
        string = request.POST.get('keyword').lower()
        isTitle = request.POST.get('option1')
        isAuthor = request.POST.get('option2')
        # now filter
        books = __getBooksList()
        newBooks = []
        for item in books:
            contained = False
            if isTitle and string in item['title'].lower():
                contained = True
            if not contained and isAuthor and string in item['author'].lower():
                contained = True
            if contained: 
                newBooks.append(item)
        return render(request, 'bookmodule/bookList.html', {'books':newBooks})
    return render(request,'bookmodule/search.html')

### lab 7
def simple_query(request):
    mybooks=Book.objects.filter(title__icontains='and') # <- multiple objects
    return render(request, 'bookmodule/bookList.html', {'books':mybooks})

def complex_query(request):
    mybooks = Book.objects.filter(
        author__isnull=False,  # Ensures author is not null
        title__icontains='the',  # Filters books with 'and' in title
        edition__gte=2,  # Selects books with edition >= 2
        price__lte=100 , # Excludes books with price <= 100
    )[:10]  # Limits results to 10 books
    if mybooks.exists():
        return render(request, 'bookmodule/bookList.html', {'books': mybooks})
    else:
        return render(request, 'bookmodule/index.html')
    
### lab 8
def models_lab8(request):
    #task 1
    task1_books = Book.objects.filter(Q(price__lte=30))

    #task 2
    task2_books = Book.objects.filter(Q(edition__gt=2) & (Q(title__icontains='qu') | Q(author__icontains='qu')))

    #task 3
    task3_books = Book.objects.filter(~(Q(edition__gt=2) & (Q(title__icontains='qu') | Q(author__icontains='qu'))))

    #task 4
    task4_books = Book.objects.all().order_by('title')

    #task 5
    book_stats = Book.objects.aggregate(
        total_books=Count('id'),
        total_price=Sum('price'),
        avg_price=Avg('price'),
        max_price=Max('price'),
        min_price=Min('price')
    )

    return render(request, 'bookmodule/lab8.html', {
        'task1_books': task1_books,
        'task2_books': task2_books,
        'task3_books': task3_books,
        'task4_books': task4_books,
        'book_stats': book_stats,
    })

#lab 9
def models_lab9(request):
     #task 2: 
    publishers_with_stock = Publisher.objects.annotate(stock_counter=Count('book9'))

    #task 3: 
    oldest_pubdate = Publisher.objects.aggregate(oldest_pubdate=Min('book9__pubdate'))

    #task 4: 
    publishers_with_avg_price = Publisher.objects.annotate(avg_price=Avg('book9__price'))

    #task 5: 
    publishers_book_count_filtered = Publisher.objects.annotate(
        book_count=Count('book9', filter=Q(book9__price__gt=50))
    )
    context = {
        'publishers_with_stock': publishers_with_stock,
        'oldest_pubdate': oldest_pubdate,
        'publishers_with_avg_price': publishers_with_avg_price,
        'publishers_book_count_filtered': publishers_book_count_filtered,
    }

    return render(request, 'bookmodule/lab9.html', context)


#lab 10 
def list_books(request): # task 1 -1
    books = Book10.objects.all()
    return render(request, 'bookmodule/lab10.html', {'books': books, 'mode': 'list'})


def add_book(request): # taskk 2 -1

    if request.method == 'POST':
        title = request.POST['title']
        price = request.POST['price']
        edition = request.POST['edition']
        author_name = request.POST['author_name']
        
        author, created = Author.objects.get_or_create(name=author_name)

        Book10.objects.create(title=title, price=price, edition=edition, author=author)
        return redirect('list_books')

    return render(request, 'bookmodule/lab10.html', {'mode': 'add'})



def edit_book(request, id): # task 3- 1
    book = get_object_or_404(Book10, id=id)
    if request.method == 'POST':
        book.title = request.POST['title']
        book.price = request.POST['price']
        book.edition = request.POST['edition']
        author_name = request.POST['author_name'].strip().title()
        author, _ = Author.objects.get_or_create(name=author_name)
        book.author = author
        book.save()
        return redirect('list_books')
    authors = Author.objects.all()
    return render(request, 'bookmodule/lab10.html', {'book': book, 'authors': authors, 'mode': 'edit'})


def delete_book(request, id): # task 4-1
    book = get_object_or_404(Book10, id=id)
    if request.method == 'POST':
        book.delete()
        return redirect('list_books')
    return render(request, 'bookmodule/lab10.html', {'book': book, 'mode': 'delete'})


# ----


def list_books_form(request): # task 1-2 
    books = Book10.objects.all()
    return render(request, 'bookmodule/lab10.html', {'books': books, 'mode': 'list_form'})


def add_book_form(request): # task 2 -2
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_books_form')
    else:
        form = BookForm()
    return render(request, 'bookmodule/lab10.html', {'form': form, 'mode': 'add_form'})


def edit_book_form(request, id): # task 3-2
    book = get_object_or_404(Book10, id=id)
    form = BookForm(request.POST or None, instance=book)
    if form.is_valid():
        form.save()
        return redirect('list_books_form')
    return render(request, 'bookmodule/lab10.html', {'form': form, 'mode': 'edit_form'})


def delete_book_form(request, id): #task 4-4
    book = get_object_or_404(Book10, id=id)
    if request.method == 'POST':
        book.delete()
        return redirect('list_books_form')
    return render(request, 'bookmodule/lab10.html', {'book': book, 'mode': 'delete_form'})


# lab 11 - 
# Task 1
@login_required(login_url='login')
def list_books_lab11(request):
    books = Book11.objects.all()
    return render(request, 'bookmodule/lab11.html', {'books': books, 'mode': 'list_books'})


@login_required(login_url='login')
def add_book_lab11(request):
    if request.method == 'POST':
        form = Book11Form(request.POST)
        if form.is_valid():
            book = form.save(commit=False)  
            book.save()
            form.save_m2m()
            return redirect('list_books_lab11')
    else:
        form = Book11Form()
    return render(request, 'bookmodule/lab11.html', {'form': form, 'mode': 'add_book'})


@login_required(login_url='login')
def edit_book_lab11(request, book_id):
    book = get_object_or_404(Book11, id=book_id)
    if request.method == 'POST':
        form = Book11Form(request.POST, instance=book)
        if form.is_valid():
            book = form.save(commit=False)  
            book.save()
            form.save_m2m()
            return redirect('list_books_lab11')
    else:
        form = Book11Form(instance=book)
    return render(request, 'bookmodule/lab11.html', {'form': form, 'book': book, 'mode': 'edit_book'})


@login_required(login_url='login')
def delete_book_lab11(request, book_id):
    book = get_object_or_404(Book11, id=book_id)
    if request.method == 'POST':
        book.delete()
        return redirect('list_books_lab11')
    return render(request, 'bookmodule/lab11.html', {'book': book, 'mode': 'delete_book'})


# Task 2
@login_required(login_url='login')
def list_books_with_cover(request):
    books = BookWithCover.objects.all()
    return render(request, 'bookmodule/lab11.html', {'books': books, 'mode': 'list_books_with_cover'})


@login_required(login_url='login')
def add_book_with_cover(request):
    if request.method == 'POST':
        form = BookWithCoverForm(request.POST, request.FILES)
        if form.is_valid():
            book = form.save(commit=False)  
            book.save()
            form.save_m2m()
            return redirect('list_books_with_cover')
    else:
        form = BookWithCoverForm()
    return render(request, 'bookmodule/lab11.html', {'form': form, 'mode': 'add_book_with_cover'})


@login_required(login_url='login')
def edit_book_with_cover(request, book_id):
    book = get_object_or_404(BookWithCover, id=book_id)
    if request.method == 'POST':
        form = BookWithCoverForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            book = form.save(commit=False)  
            book.save()
            form.save_m2m()
            return redirect('list_books_with_cover')
    else:
        form = BookWithCoverForm(instance=book)
    return render(request, 'bookmodule/lab11.html', {'form': form, 'book': book, 'mode': 'edit_book_with_cover'})

@login_required(login_url='login')
def delete_book_with_cover(request, book_id):
    book = get_object_or_404(BookWithCover, id=book_id)
    if request.method == 'POST':
        book.delete()
        return redirect('list_books_with_cover')
    return render(request, 'bookmodule/lab11.html', {'book': book, 'mode': 'delete_book_with_cover'})


#lab 13
def lab12_task1(request):
    return render(request, 'bookmodule/lab12_task1.html')

def lab12_task2(request):
    return render(request, 'bookmodule/lab12_task2.html')

def lab12_task3(request):
    return render(request, 'bookmodule/lab12_task3.html')

def lab12_task4(request):
    return render(request, 'bookmodule/lab12_task4.html')

def lab12_task5(request):
    return render(request, 'bookmodule/lab12_task5.html')




