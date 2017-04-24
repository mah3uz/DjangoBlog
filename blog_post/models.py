from django.db import models

class BlogPost(models.Model):
    title = models.CharField(max_length=120)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)