from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from bookmark.models import Bookmark
from django.urls import reverse_lazy

# Create your views here.

class BookmarkLV(ListView):
    model =  Bookmark

class BookmarkDV(DetailView):
    model = Bookmark

class BookmarkCV(CreateView):
    model = Bookmark
    fields = ['title', 'url']
    template_name_suffix = '_create'
    success_url = reverse_lazy('bookmark_index')

class BookmarkUV(UpdateView):
    model = Bookmark
    fields = ['title', 'url']
    template_name_suffix = '_update'
    success_url = reverse_lazy('bookmark_index')


class BookmarkRV(DeleteView):
    model = Bookmark
    success_url = reverse_lazy('bookmark_index')


