from rest_framework import serializers

from .models import Author, Book


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author  # fields and validation are derived from the model
        fields = ["id", "name", "country"]


class BookSerializer(serializers.ModelSerializer):
    # Extra read-only output field, taken from the related author
    author_name = serializers.CharField(source="author.name", read_only=True)

    class Meta:
        model = Book
        fields = ["id", "title", "year", "author",
                  "author_name"]  # author = the id

    # validate_<field> runs after the basic type check, like a Pydantic validator
    def validate_year(self, value):
        if not 1000 <= value <= 2100:
            raise serializers.ValidationError(
                "Year must be between 1000 and 2100")
        return value
