from django.db import models

# Create your models here.

class PostAttachments(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    post_id = models.IntegerField(blank=False)
    zip = models.CharField(max_length=255)

    def __str__(self):
        return f'Attachments of Post {self.post_id}'

