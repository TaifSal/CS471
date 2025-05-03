from django.db import models
from django.utils import timezone 

# lab-7
#class Book(models.Model):
#    title = models.CharField(max_length = 50)
#    author = models.CharField(max_length = 50)
#    price = models.FloatField(default = 0.0)
#    edition = models.SmallIntegerField(default = 1)

# lab-8
class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    edition = models.IntegerField()

    def __str__(self):
        return self.title


# lab-9
class Publisher(models.Model):
    name = models.CharField(max_length = 100)
    location = models.CharField(max_length=300)

class Author(models.Model):
    name = models.CharField(max_length = 300)
    def __str__(self):
        return self.name 

class Book9(models.Model): 
    title = models.CharField (max_length= 50)
    price = models.DecimalField(max_digits=10, decimal_places=2) 
    rating = models.SmallIntegerField(default = 1)
    pubdate = models.DateTimeField(default=timezone.now)
    authors = models.ManyToManyField(Author) 
    publisher = models.ForeignKey(Publisher, on_delete= models.CASCADE, null=True)
    class Meta:
        ordering = ['title']

# lab 10
class Book10(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey('Author', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    edition = models.IntegerField()

    def __str__(self):
        return self.title


# lab 11 
# Task 1
class Author11(models.Model):
    fullname = models.CharField(max_length=100, null=False)
    address = models.TextField(max_length=500, null=True)
    
    def __str__(self):
        return self.fullname

class Book11(models.Model):
    title = models.CharField(max_length=100, null=False)
    price = models.FloatField(default=0)
    edition = models.IntegerField(default=1)
    authors = models.ManyToManyField(Author11)
    
    def __str__(self):
        return self.title


# Task 2
class BookWithCover(models.Model):
    title = models.CharField(max_length=100, null=False)
    price = models.FloatField(default=0)
    edition = models.IntegerField(default=1)
    authors = models.ManyToManyField(Author11)
    cover_page = models.ImageField(upload_to='book_covers/', null=True, blank=True)
    
    def __str__(self):
        return self.title
    
