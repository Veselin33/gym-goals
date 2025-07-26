from django.urls import path

from posts.views import PostListView, PostCreateView

urlpatterns = [
    path('', PostListView.as_view(), name='post-list'),
    path('add-post/', PostCreateView.as_view(), name='add-post'),

]