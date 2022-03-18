from django.http import HttpResponse
from django.shortcuts import render
from catalog.models import Books
from django.views import View


class MainView(View):
    def get(self, request):
        novelties = Books.objects.all().order_by('date')[:4]
        bestsellers = Books.objects.all().order_by('id')[:4]
        context = {
            'novelties': novelties,
            'bestsellers': bestsellers
        }
        return render(request, 'home.html', context)


class SitemapView(View):
    def get(self, request):
        return render(request, 'sitemap.xml', None, content_type="application/xhtml+xml")



