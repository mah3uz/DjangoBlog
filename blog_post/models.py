from django.db import models

STATUS_CHOICES = (
    ('d', 'Draft'),
    ('p', 'Published'),
    ('w', 'Withdrawn'),
)

class BlogPost(models.Model):
    title = models.CharField(max_length=120)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey('blog_post.Categories', blank=True, null=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='p')
    post_image = models.ImageField(null=True)

    def __str__(self):
        return self.title

class Categories(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

