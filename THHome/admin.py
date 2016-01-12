from django.contrib.admin import ModelAdmin, site
from django.contrib.auth.models import Group

from .models import Expose, Image, RealEstate


class RealEstateAdmin(ModelAdmin):
    """
    ModelAdmin class for real estate.
    """
    list_display = ('id', 'title', 'rooms', 'size', 'online',)
    list_display_links = ('id', 'title',)


site.register(RealEstate, RealEstateAdmin)
site.register(Image)
site.register(Expose)
site.unregister(Group)
