from django.db import models

# Create your models here.
class Blog(models.Model):
    thumbnail = models.ImageField(upload_to='thumbnails/')
    title = models.TextField()
    summary = models.TextField()
    body = models.TextField()
    last_updated = models.DateTimeField(auto_now=True)
