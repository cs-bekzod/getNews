from django.urls import path
from .views import NewsListCreateView, NewsDetailView

urlpatterns = [
    path('api/news/', NewsListCreateView.as_view(), name='news-list-create'),
    path('api/news/<int:pk>/', NewsDetailView.as_view(), name='news-detail')
]