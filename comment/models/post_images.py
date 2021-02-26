from django.db import models
# Create your models here.

class PostImages(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    post_id = models.IntegerField(blank=False)
    image = models.CharField(max_length=255)

    def __str__(self):
        return f'Images of Post {self.post_id}'

