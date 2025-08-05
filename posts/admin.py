from django.contrib import admin

from posts.models import Post


# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    model = Post
    list_display = ('title', 'content', 'author')
    exclude = ('author',)

    def save_model(self, request, obj, form, change):
        if not change:
            obj.author = request.user
            super().save_model(request, obj, form, change)
