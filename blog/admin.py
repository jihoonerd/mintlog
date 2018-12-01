from markdownx.admin import MarkdownxModelAdmin
from .models import Post
import tagulous


class PostAdmin(MarkdownxModelAdmin):
    list_display = ('title', 'author', 'post_tag', 'published_at', 'status')
    prepopulated_fields = {'slug': ('title',)}
    ordering = ['-published_at']
    list_filter = ['post_tag', 'published_at', 'status']
    search_fields = ['title', 'description', 'contents']


# Use tagulous.admin to employ the functionality provided by tagulous package.
tagulous.admin.register(Post, PostAdmin)