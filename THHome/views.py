from django.views.generic import DetailView, ListView

from .models import RealEstate


class Home(ListView):
    """
    View for the home page.
    """
    queryset = RealEstate.objects.filter(online=True)
    template_name = 'index.html'


class Detail(DetailView):
    """
    View for details to a real estate.
    """
    queryset = RealEstate.objects.filter(online=True)
    template_name = 'detail.html'
