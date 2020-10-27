from django.urls import path
from bookmark import views
app_name = 'bookmark'
urlpatterns = [
    path('', views.BookmarkListView.as_view(), name='index'),
    path('add/', views.BookmarkCreateView.as_view(), name='add'),
    path('detail/<int:pk>/', views.BookmarkDetailView.as_view(), name='detail'),
    path('update/<int:pk>', views.BookmarkUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', views.BookmarkDeleteView.as_view(), name='delete'),
    ]