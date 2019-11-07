from django.shortcuts import render, get_object_or_404, get_list_or_404
from wiki.models import Page
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView


class PageList(ListView):
    model = Page

    def get(self, request):
        """ Returns a list of wiki pages. """
        wiki_pages = get_list_or_404(Page)
        context = {
            'wiki_pages': wiki_pages,
        }
        return render(request, 'list.html', context)
        


class PageDetailView(DetailView):
    model = Page

    def get(self, request, slug):
        """ Returns a specific of wiki page by slug. """
        page = get_object_or_404(Page, slug=slug)
        context = {
            'wiki_page': page,
        }
        return render(request, 'page.html', context)

    def post(self, request, slug):
        pass
