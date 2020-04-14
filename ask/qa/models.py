from django.db import models
from django.contrib.auth.models import User


class QuestionManager(models.Manager):
    @staticmethod
    def new():
        return Question.objects.all().order_by('-pk')

    @staticmethod
    def popular():
        return Question.objects.all().order_by('-rating')

class Question(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default=0)
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    likes =  models.ManyToManyField(User, related_name='question_like_user')
    objects = QuestionManager()



class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True)
    question = models.ForeignKey(Question, null=True, on_delete=models.SET_NULL)
    author =  models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

