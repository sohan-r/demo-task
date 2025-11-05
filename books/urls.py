from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet, sync_external_posts, books_by_genre_report

router = DefaultRouter()
router.register(r'books', BookViewSet, basename='book')


urlpatterns = [
    path("api/", include(router.urls)),
    path("api/sync-external-posts/", sync_external_posts, name="sync-external-posts"),
    path("reports/books-by-genre/", books_by_genre_report, name="books-by-genre-report"),
]
