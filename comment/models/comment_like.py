from django.db import models
from .comment import Comment
# Create your models here.

class CommentLike(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    comment_id = models.ForeignKey(Comment, on_delete=models.CASCADE, blank=False)
    user_id = models.IntegerField(blank=False)
    
    class Meta:
        unique_together = ['comment_id', 'user_id']
    def __str__(self):
        return f'CommentLike of {self.comment_id}'