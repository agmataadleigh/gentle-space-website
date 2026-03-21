from django.db import models
from django.utils import timezone

class Post(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    likes = models.IntegerField(default=0)

    def __str__(self):
        return self.content[:30]