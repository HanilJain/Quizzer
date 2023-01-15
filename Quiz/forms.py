from django import forms
from django.contrib.auth.models import User
from .models import Question , Answer

class QuestionCreateForm(forms.ModelForm):
    question = forms.CharField()
    class Meta :
        model = Question
        fields = ['question'] 

class AnswerCreateForm(forms.ModelForm):
    option_1 = forms.CharField()
    option_2 = forms.CharField()
    option_3 = forms.CharField()
    option_4 = forms.CharField()
    option1_is_correct = forms.BooleanField(required=False)
    option2_is_correct = forms.BooleanField(required=False)
    option3_is_correct = forms.BooleanField(required=False)
    option4_is_correct = forms.BooleanField(required=False)

    class Meta : 
        model = Answer
        fields = ['option_1','option1_is_correct','option_2','option2_is_correct','option_3','option3_is_correct','option_4','option4_is_correct']

