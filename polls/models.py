from django.db import models
from django.db.models import Count

# Create your models here.


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    answer = models.ManyToManyField('Answer')

    def __str__(self):
        return self.question_text
    

class Answer(models.Model):
    answer = models.CharField(max_length=300)

    def __str__(self):
        return self.answer

    def response_count(self):
        return Response.objects.filter(answer=self.answer).count()



class Response(models.Model):
    question = models.ForeignKey('Question',on_delete=models.CASCADE,null=True, blank=True)
    answer = models.ForeignKey('Answer',on_delete=models.CASCADE,null=True, blank=True)

    def __str__(self):
        return f'{self.answer.answer}'

