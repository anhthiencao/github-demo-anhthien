from django.contrib import admin
from .models import Comment, CommentLike, PostAuth, PostInteract, PostAttachments, PostImages


# Register your models here.
models_list = [
    Comment,
    CommentLike,
    PostAuth,
    PostInteract,
    PostAttachments,
    PostImages,
]
admin.site.register(models_list)