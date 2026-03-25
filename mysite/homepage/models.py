from django.db import models

class Post(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_auto_now_add=True)
    likes = models.IntegerField(default=0)

    def __str__(self):
        return self.content[:30]