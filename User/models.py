from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class quiztaker(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.user.username} Name'

class quizmaster(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.user.username}'