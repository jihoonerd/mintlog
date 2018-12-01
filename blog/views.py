from django.views.generic import ListView, DetailView
from .filters import PostFilter
from .models import Post


class PostListView(ListView):
    model = Post
    template_name = 'post_list.html'
    paginate_by = 9

    def get_queryset(self):
        return PostFilter(self.request.GET, queryset=Post.objects.all()).qs

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        post_tag = self.request.GET.get('post_tag', default='ALL')
        context['tags'] = self.model.post_tag.tag_model.objects.all()
        context['filter_tag'] = post_tag
        return context


class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'