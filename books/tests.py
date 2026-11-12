from rest_framework.test import APITestCase

from .models import Author


class BookApiTests(APITestCase):
    def setUp(self):
        self.author = Author.objects.create(name="Tolkien", country="UK")

    def test_anonymous_cannot_create(self):
        res = self.client.post(
            "/api/books/", {"title": "X",
                            "year": 2000, "author": self.author.id}
        )
        self.assertEqual(res.status_code, 403)

    def test_invalid_min_year(self):
        res = self.client.get("/api/books/", {"min_year": "abc"})
        self.assertEqual(res.status_code, 400)
