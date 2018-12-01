import django_filters
from .models import Portfolio


class PortfolioFilter(django_filters.FilterSet):

    class Meta:
        model = Portfolio
        fields = ['portfolio_tag']

    @property
    def qs(self):
        parent = super(PortfolioFilter, self).qs
        return parent.filter(status='published').order_by('-published_at')