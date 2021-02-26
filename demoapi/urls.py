"""demoapi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from comment.views import (
    CommentListView, CommentDetailView, 
    CommentLikeListView, CommentLikeDetailView,
    PostAuthListView, PostAuthDetailView,
    PostInteractListView, PostInteractDetailView,
    PostAttachmentsListView, PostAttachmentsDetailView,
    PostImagesListView, PostImagesDetailView
)

urlpatterns = [
    path('admin/', admin.site.urls),

    path('comment/', CommentListView.as_view()),
    path('comment/<int:pk>/', CommentDetailView.as_view()),

    path('comment_like/', CommentLikeListView.as_view()),
    path('comment_like/<int:pk>/', CommentLikeDetailView.as_view()),

    path('post_auth/', PostAuthListView.as_view()),
    path('post_auth/<int:pk>/', PostAuthDetailView.as_view()),

    path('post_interact/', PostInteractListView.as_view()),
    path('post_interact/<int:pk>/', PostInteractDetailView.as_view()),

    path('post_attachments/', PostAttachmentsListView.as_view()),
    path('post_attachments/<int:pk>/', PostAttachmentsDetailView.as_view()),

    path('post_images/', PostImagesListView.as_view()),
    path('post_images/<int:pk>', PostImagesDetailView.as_view()),
]

