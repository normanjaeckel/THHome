from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^$', views.Home.as_view(), name='home'),
    url(r'^(?P<pk>\d+)/$', views.Detail.as_view(), name='detail'),
    url(r'^admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
