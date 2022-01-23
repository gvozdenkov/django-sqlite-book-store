from unicodedata import name
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='all-books'),
    path('<slug:slug>', views.book_detail, name='book-detail-page')
]
