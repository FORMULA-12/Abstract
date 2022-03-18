from django.urls import path
from .views import MainView, SitemapView


urlpatterns = [
    path('', MainView.as_view(), name='home'),
    path('sitemap', SitemapView.as_view(), name='sitemap'),
]