from rest_framework import viewsets
from rest_framework.exceptions import ValidationError

from .models import Author, Book
from .serializers import AuthorSerializer, BookSerializer


# list, create, retrieve, update, delete
class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.order_by("id")  # pagination needs a stable order
    serializer_class = AuthorSerializer


class BookViewSet(viewsets.ModelViewSet):
    serializer_class = BookSerializer

    def get_queryset(self):
        # select_related joins the author, so author_name costs no extra queries
        qs = Book.objects.select_related("author").order_by("id")
        min_year = self.request.query_params.get(
            "min_year")  # /api/books/?min_year=1950
        if min_year is not None:
            try:
                qs = qs.filter(year__gte=int(min_year))
            except ValueError:
                # A clean 400 instead of the 500 we got with ?min_year=abc
                raise ValidationError({"min_year": "must be an integer"})
        return qs
