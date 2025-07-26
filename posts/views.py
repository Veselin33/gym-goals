from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
from posts.forms import PostForm
from posts.models import Post


# Create your views here.


class PostCreateView(LoginRequiredMixin ,CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add-post.html'
    success_url = reverse_lazy('post-list')
    ordering = ('-created',)

    def form_valid(self, form):
        post = form.save(commit=False)
        post.author = self.request.user
        post.save()
        return super().form_valid(form)

class PostListView(ListView):
    model = Post
    template_name = 'posts_list.html'
