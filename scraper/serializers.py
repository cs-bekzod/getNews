from rest_framework import serializers

class NewsSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    content = serializers.CharField()
    link = serializers.URLField()
    published_at = serializers.CharField(max_length=100)
    