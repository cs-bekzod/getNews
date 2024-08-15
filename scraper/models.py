from django.db import models

class NewsArticle(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    link = models.URLField(unique=True)
    published_at = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    datetime_format = models.CharField(max_length=100)

    def __str__(self):
        return self.title
