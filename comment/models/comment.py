from django.db import models

# Create your models here.

class Comment(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    message = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True, blank=False)
    edited_at = models.DateTimeField(auto_now=True, blank=False)
    user_id = models.IntegerField(blank=False)
    post_id = models.IntegerField(blank=False)
    parent_id = models.IntegerField(blank=True)

    def __str__(self):
        return f'Comment {self.id} of Post {self.post_id}'

