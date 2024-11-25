from django.shortcuts import render
from .models import Book, Category

# Create your views here.

data = {

}


def home(request):
    context = {
        'books': Book.objects.filter(is_home=True),
        'categories': Category.objects.all()

    }
    return render(request, 'book/home.html', context)

def books(request):
    context = {
        'books': Book.objects.all(),
        'categories': Category.objects.all()
    }
    return render(request, 'book/books.html', context)

def book_details(request, slug):
    book = Book.objects.get(slug=slug)
    return render(request, 'book/book_details.html',{"book": book})

def book_by_category(request, slug):
    context = {
        "books": Category.objects.get(slug=slug).book_set.all(),
        "categories": Category.objects.all(),
        "selected_category": slug
    }
    return render(request, 'book/books.html', context)