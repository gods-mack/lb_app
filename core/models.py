from django.db import models

# Create your models here.


class UserPost(models.Model):
    id = models.AutoField(primary_key=True)
    media_url = models.CharField(max_length=255)
    caption = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.caption

    def serializer(self):
        return {
            'id': self.id,
            'media_url': self.media_url,
            'caption': self.caption,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }

    class Meta:
        ordering = ['-created_at']