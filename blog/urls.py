# blog/urls.py
from django.urls import path
from blog.views import (
    post_list, post_create, post_detail, post_edit, post_delete
)

urlpatterns = [
    path("", post_list, name="home"),
    path("post/new/", post_create, name="post_create"),
    path("post/<int:pk>/", post_detail, name="post_detail"),
    path("post/<int:pk>/edit/", post_edit, name="post_edit"),
    path("post/<int:pk>/delete/", post_delete, name="post_delete")
]