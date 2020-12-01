from django.urls import path
from polls import views
app_name = 'polls'
urlpatterns = [

    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('<int:pk>/result/', views.Result.as_view(), name='result'),
    path('<int:question_id>/reset/', views.reset, name='reset'),


    path('choice_add/', views.ChoiceCV.as_view(), name='choice_add'),


    path('question_add/',views.QuestionCV.as_view(),name='question_add'),

]
