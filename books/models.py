from django.db import models


class Author(models.Model):  # table "books_author"; Django adds the id column itself
    name = models.CharField(max_length=100)
    # text uses "" instead of NULL
    country = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.name  # how an author shows up in the admin


class Book(models.Model):
    title = models.CharField(max_length=200)
    year = models.IntegerField()
    # on_delete is required: CASCADE deletes an author's books with the author
    # related_name="books" lets you write author.books
    author = models.ForeignKey(
        Author, on_delete=models.CASCADE, related_name="books")
    pages = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.title
