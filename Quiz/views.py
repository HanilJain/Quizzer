from django.shortcuts import render
from django.http import HttpRequest
from django.views.generic import ListView,DetailView
from .models import Quiz ,Question ,Answer
# Create your views here.


def home(request):
    return render(request , 'User/home.html' )
    
class QuizListView(ListView):
    model = Quiz
    template_name = 'Quiz/quiz_home.html'
    context_object_name = 'quiz'

class QuizDetailView(DetailView):
    model = Quiz
    template_name = 'Quiz/quiz_information.html'
    
class QuestionListView(ListView):
    model = Question
    template_name = 'Quiz/question.html'
    context_object_name = 'question'
    
    def get_context_data(self, **kwargs) :
        context = super().get_context_data(**kwargs)
        context = Answer.objects.all()
        content = {'context' : context}
        return content

def QuestionView(request , id ):
    ques = Question.objects.all()
    ans = Answer.objects.all()
    quiz = Quiz.objects.all()
    id_no = Quiz.objects.get(id = id)
    content = { 'id' : id_no ,'quiz' : quiz , 'question' : ques , 'answer' : ans}
    return render(request , 'Quiz/question.html' , content)