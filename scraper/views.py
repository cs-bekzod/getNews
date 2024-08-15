from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework import generics, filters
from rest_framework.views import APIView
from .serializers import NewsSerializer
from .models import NewsArticle
from .utils import get_news

class NewsListCreateView(generics.ListCreateAPIView):
    queryset = NewsArticle.objects.all()
    serializer_class = NewsSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title']
    ordering_fields = ['datetime_format']
    
class NewsDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = NewsArticle.objects.all()
    serializer_class = NewsSerializer


