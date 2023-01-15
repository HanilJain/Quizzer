from django.urls import path
from . import views
from .views import QuizListView , QuizDetailView , QuizCreateView

urlpatterns = [

    path('', views.home , name='home'), #.as_view() is used to make class a view
    path('home/' , QuizListView.as_view() , name='quiz-home'),
    path('<int:pk>/instruction/' , QuizDetailView.as_view() , name='quiz-instruction'),
    path('<id>/question/' , views.QuestionView , name='questions'),
    path('new/' , QuizCreateView.as_view() , name='new-quiz'),
    path('<id>/add-question/', views.QuestionCreateView , name='new-ques'),
]
