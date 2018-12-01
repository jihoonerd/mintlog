from django.views.generic import ListView, DetailView
from .filters import PortfolioFilter
from .models import Portfolio


class PortfolioListView(ListView):
    model = Portfolio
    template_name = 'portfolio_list.html'
    paginate_by = 6

    def get_queryset(self):
        return PortfolioFilter(self.request.GET, queryset=Portfolio.objects.all()).qs

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        portfolio_tag = self.request.GET.get('portfolio_tag', default='ALL')
        context['tags'] = self.model.portfolio_tag.tag_model.objects.all()
        context['filter_tag'] = portfolio_tag
        return context


class PortfolioDetailView(DetailView):
    model = Portfolio
    template_name = 'portfolio_detail.html'