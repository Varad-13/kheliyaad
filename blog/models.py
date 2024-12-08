from django.db import models

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

class Blog(models.Model):
    thumbnail = models.ImageField(upload_to='thumbnails/')
    title = models.TextField()
    summary = models.TextField()
    tags = models.ManyToManyField(Tag, related_name='blogs')
    body = models.TextField()
    body_html = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
