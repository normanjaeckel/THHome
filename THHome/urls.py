# -*- coding: utf-8 -*-

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import re_path

from . import views

urlpatterns = [
    re_path(r'^$', views.Home.as_view(), name='home'),
    re_path(r'^impressions/$',
        views.Impressions.as_view(),
        name='impressions_all'),
    re_path(r'^(?P<pk>\d+)/$', views.Detail.as_view(), name='detail'),
    re_path(r'^admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
