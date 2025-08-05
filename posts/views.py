from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DeleteView
from posts.forms import PostForm
from posts.models import Post


# Create your views here.


class PostCreateView(LoginRequiredMixin ,CreateView):
    model = Post
    form_class = PostForm
    template_name = 'posts/add-post.html'
    success_url = reverse_lazy('post-list')

    def form_valid(self, form):
        post = form.save(commit=False)
        post.author = self.request.user
        post.save()
        return super().form_valid(form)

class PostListView(ListView):
    model = Post
    template_name = 'posts/posts_list.html'
    ordering = ['-created_at']

class DeletePostView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Post
    template_name = 'posts/delete-post.html'
    success_url = reverse_lazy('post-list')
    permission_required = 'posts.delete_post'

    def handle_no_permission(self):
        messages.error(self.request, "You do not have permission to delete posts.")
        return redirect('post-list')
