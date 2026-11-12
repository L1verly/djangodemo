from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
# has a queryset, the name is inferred
router.register("authors", views.AuthorViewSet)
# basename needed: no queryset attribute
router.register("books", views.BookViewSet, basename="book")

urlpatterns = router.urls  # generates /authors/, /authors/<id>/, /books/, ...
