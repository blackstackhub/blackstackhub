from django.urls import path, re_path
from django.views.generic.base import RedirectView
from . import views
urlpatterns = [
    path('', views.home, name='Home'),
    re_path(r'^.*$', RedirectView.as_view(pattern_name='Home', permanent=False)),
]
