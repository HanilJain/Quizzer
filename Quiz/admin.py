from django.contrib import admin
from .models import Quiz , Question , Answer , Marks_Of_User

# Register your models here.

mymodel = [Quiz, Question , Answer , Marks_Of_User]
admin.site.register(mymodel)