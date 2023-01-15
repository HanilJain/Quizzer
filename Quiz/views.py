from django.shortcuts import render , redirect
from django.http import HttpRequest 
from django.contrib import messages
from django.views.generic import ListView,DetailView , CreateView
from .models import Quiz ,Question ,Answer
from . forms import QuestionCreateForm , AnswerCreateForm 
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
    
def QuestionView(request , id ):
    ques = Question.objects.all()
    ans = Answer.objects.all()
    quiz = Quiz.objects.all()
    id_no = Quiz.objects.get(id = id)
    content = { 'id' : id_no ,'quiz' : quiz , 'question' : ques , 'answer' : ans}
    return render(request , 'Quiz/question.html' , content)


class QuizCreateView(CreateView): 
    model = Quiz
    fields=['name','desc' , 'number_of_questions' , 'time'] # form for creating post
    template_name = 'Quiz/add_quiz.html'


def QuestionCreateView(request, id):

    if request.method == 'POST' :
        q_form = QuestionCreateForm( request.POST )
        a_form = AnswerCreateForm( request.POST )
        
        if q_form.is_valid() & a_form.is_valid():
            q_form.save()
            a_form.save()
            messages.success(request , f'Question Successfully Uploaded ! ')
            
    else :
        q_form = QuestionCreateForm()
        a_form = AnswerCreateForm()
    
    context = { 
            'q_form' : q_form , 
            'a_form' : a_form , 
            }

    return render(request , 'Quiz/add_question.html' , context )



