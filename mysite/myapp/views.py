from django.shortcuts import render
from .models import Book
from functools import lru_cache

# кеширует результаты функции в памяти.


@lru_cache(maxsize=None)  # maxsize=None означает, что кеш неограниченного размера
def cached_book_list(request):
    books = Book.objects.all()
    return render(request, 'myapp/book_list.html', {'books': books})


def book_list(request):
    books = cached_book_list(request)
    return render(request, 'myapp/book_list.html', {'books': books})
