from django.urls import path
from . import views



urlpatterns = [
    path("", views.home, name='home'),
    path("books/", views.books, name='books'),
    path("books/<slug:slug>", views.book_details, name='book_details'),
    path('category/<slug:slug>', views.book_by_category, name='book_by_category')
]