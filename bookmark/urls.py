from django.urls import path
from bookmark import views
app_name = 'bookmark'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('add/', views.BookmarkCreateView.as_view(), name='create'),

    ]