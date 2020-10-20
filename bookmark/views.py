from django.views import generic
from .models import Bookmark
from django.urls import reverse_lazy

class BookmarkListView(generic.ListView):
    model = Bookmark

class BookmarkCreateView(generic.CreateView):
    model = Bookmark
    fields = ['site_name', 'url']
    success_url = reverse_lazy('bookmark:index') # url 패턴이름으로 url스트링 구함. 앱이름 꼭 쓰기
    template_name_suffix = '_create'

class BookmarkDetailView(generic.DetailView):
    model = Bookmark

class BookmarkUpdateView(generic.UpdateView):
    model = Bookmark
    fields = ['site_name', 'url']
    success_url = reverse_lazy('bookmark:index')
    template_name_suffix = '_update'