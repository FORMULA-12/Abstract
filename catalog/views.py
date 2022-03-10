from django.shortcuts import render
from .models import Books
from django.views import View


class MainView(View):
    def get(self, request):

        if 'search' in request.GET and request.GET['search']:
            data = request.GET['search']
            books = Books.objects.filter(title__icontains=data).order_by('id')
            context = {
                'books': books
            }
        elif 'language' in request.GET and request.GET['language']:
            data = request.GET['language']
            books = Books.objects.filter(language__icontains=data).order_by('id')
            context = {
                'books': books
            }
        elif 'category' in request.GET and request.GET['category']:
            data = request.GET['category']
            books = Books.objects.filter(category__icontains=data).order_by('id')
            context = {
                'books': books
            }
        else:
            books = Books.objects.all().order_by('id')
            context = {
                'books': books
            }
        return render(request, 'catalog.html', context)


