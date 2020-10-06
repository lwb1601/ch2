from django.shortcuts import render
from django.views import generic
from .models import BookmarkSet, Bookmark
from django.urls import reverse_lazy
# Create your views here.

class IndexView(generic.ListView):
    model = BookmarkSet

class DetailView(generic.DetailView):
    model = BookmarkSet

class BookmarkCreateView(generic.CreateView):
    model = Bookmark
    fields = ['title','url']
    success_url = reverse_lazy('detail')
    template_name_suffix = '_create'
