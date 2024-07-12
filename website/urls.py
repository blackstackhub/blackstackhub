from django.urls import path, re_path
from django.views.generic.base import RedirectView
from . import views

from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', views.home, name='Home'),
    path('app-ads.txt', views.ads, name='Ads'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += [re_path(r'^.*$', RedirectView.as_view(pattern_name='Home', permanent=False))]



