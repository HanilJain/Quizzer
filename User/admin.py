from django.contrib import admin
from .models import quizmaster , quiztaker

# Register your models here.
mymodel = [quizmaster,quiztaker]
admin.site.register(mymodel)