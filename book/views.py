from django.shortcuts import render
from catalog.models import Books
from django.views import View


class MainView(View):
    def get(self, request, *args, **kwargs):

        if self.kwargs.get("pk"):
            id = self.kwargs.get("pk")
            book = Books.objects.filter(id=id)
            context = {
                'book': book
            }
            return render(request, 'book.html', context)
