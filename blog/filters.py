import django_filters
from .models import Post


class PostFilter(django_filters.FilterSet):

    class Meta:
        model = Post
        fields = ['post_tag']

    @property
    def qs(self):
        parent = super(PostFilter, self).qs
        return parent.filter(status='published').order_by('-published_at')