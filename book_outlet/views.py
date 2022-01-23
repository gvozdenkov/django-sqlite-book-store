from logging.handlers import SYSLOG_UDP_PORT
from django.forms import SlugField
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.db.models import Avg, Min        #агрегатная функция среднее

from django.http import Http404

from . models import Book

# Create your views here.

def index(request):
    all_books = Book.objects.all().order_by("-rating")
    num_books = all_books.count()
    avg_rating = all_books.aggregate(Avg("rating"), Min("rating"))      # возвращает словарь rating__avg, rating__min etc

    return render(request, "book_outlet/index.html", {
        "all_books": all_books,
        "total_books": num_books,
        "average_rating": avg_rating
    })

def book_detail(request, slug):
    # получаем одну конкретную книгу по id

    # try:
    #     book = Book.objects.get(pk=id)
    # except:
    #     raise Http404()

    book = get_object_or_404(Book, slug=slug)
    return render(request, 'book_outlet/book_detail.html', {
        "title": book.title,
        "author": book.author,
        "rating": book.rating,
        "is_bestselling": book.is_bestselling
    })