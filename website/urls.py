from django.urls import path, re_path
from django.views.generic.base import RedirectView
from . import views
from django.views.generic import TemplateView
urlpatterns = [
    path('', views.home, name='Home'),
    path('ads.txt', TemplateView.as_view(template_name='ads.txt', content_type='text/plain')),
    re_path(r'^.*$', RedirectView.as_view(pattern_name='Home', permanent=False)),
]
