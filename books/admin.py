from django.contrib import admin

from .models import Author, Book

# the simplest form: full CRUD screens for the model
admin.site.register(Author)


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ["title", "year", "author"]  # columns in the list view
    list_filter = ["year"]  # sidebar filter
    search_fields = ["title"]  # search box
