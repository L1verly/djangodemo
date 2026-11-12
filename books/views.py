from django.http import JsonResponse
from django.shortcuts import render

from .models import Book


def book_list(request):
    books = Book.objects.select_related("author")  # avoid N+1 on b.author.name
    # query string: /books/?min_year=1950
    min_year = request.GET.get("min_year")
    if min_year:
        # int("abc") crashes with a 500
        books = books.filter(year__gte=int(min_year))
    data = [
        {"id": b.id, "title": b.title, "year": b.year, "author": b.author.name}
        for b in books
    ]
    return JsonResponse({"books": data})
