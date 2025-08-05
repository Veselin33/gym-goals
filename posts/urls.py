from django.urls import path

from posts.views import PostListView, PostCreateView, DeletePostView

urlpatterns = [
    path('', PostListView.as_view(), name='post-list'),
    path('add-post/', PostCreateView.as_view(), name='add-post'),
    path('post/delete/<int:pk>/', DeletePostView.as_view(), name='delete-post'),

]
