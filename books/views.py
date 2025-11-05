from rest_framework import viewsets, status
from rest_framework.decorators import action, api_view
from rest_framework.response import Response
from django.db.models import Count
from django.shortcuts import render
import requests
from .models import Book, ExternalPost
from .serializers import BookSerializer, ExternalPostSerializer

# CRUD viewset for Book
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all().order_by("-created_at")
    serializer_class = BookSerializer

# Simple endpoint to fetch external posts (example third-party API integration)
@api_view(['POST'])
def sync_external_posts(request):
    """
    Fetch posts from JSONPlaceholder and store unique ones in ExternalPost.
    """
    url = "https://jsonplaceholder.typicode.com/posts"
    r = requests.get(url, timeout=10)
    if r.status_code != 200:
        return Response({"detail": "Failed to fetch posts"}, status=502)
    added = 0
    for item in r.json():
        ext_id = item.get("id")
        if not ExternalPost.objects.filter(external_id=ext_id).exists():
            ExternalPost.objects.create(
                external_id=ext_id,
                title=item.get("title", "")[:255],
                body=item.get("body", "")
            )
            added += 1
    return Response({"fetched": len(r.json()), "added": added})


from .models import Book
import json


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


def books_by_genre_report(request):
    genre_data = Book.objects.values('genre').annotate(count=Count('id')).order_by('genre')
    data = list(genre_data)

    # Convert to JSON safely
    chart_data = json.dumps(data, ensure_ascii=False)

    return render(request, 'books/books_report.html', {'chart_data': chart_data})


