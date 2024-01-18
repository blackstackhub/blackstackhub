from django.urls import path, re_path
from django.views.generic.base import RedirectView
from . import views
from django.views.generic import TemplateView
urlpatterns = [
    path('', views.home, name='Home'),
    path('app-ads.txt', views.ads, name='Ads'),
    re_path(r'^.*$', RedirectView.as_view(pattern_name='Home', permanent=False)),
]
