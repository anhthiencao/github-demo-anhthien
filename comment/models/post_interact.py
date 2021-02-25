from django.db import models

# Create your models here.

class PostInteract(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    post_id = models.IntegerField(blank=False)
    user_id = models.IntegerField(blank=False)
    type = models.IntegerField(blank=False)

    def __str__(self):
        return f'Interact of Post {self.post_id}'