from django.views.generic import DetailView, ListView

from .models import Deal, Impression, RealEstate


class Home(ListView):
    """
    View for the home page.
    """
    queryset = RealEstate.objects.filter(online=True)
    template_name = 'index.html'

    def get_context_data(self, **context):
        context['deals'] = Deal.objects.all()
        context['impressions'] = Impression.objects.all()[:5]
        return super().get_context_data(**context)


class Detail(DetailView):
    """
    View for details to a real estate.
    """
    queryset = RealEstate.objects.filter(online=True)
    template_name = 'detail.html'


class Impressions(ListView):
    """
    View for all impression images.
    """
    queryset = Impression.objects.all()
    template_name = 'impressions_all.html'
