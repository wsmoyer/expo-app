from django.db import models
from django.db.models import Count

# Create your models here.


class Question(models.Model):
    question_text = models.CharField(max_length=200)

    def __str__(self):
        return self.question_text
    

class Response(models.Model):
    response = models.TextField(blank=True)
    question = models.ForeignKey('Question',on_delete=models.CASCADE)

    def __str__(self):
        return self.response

    def response_count(self):
        return Response.objects.filter(response=self.response).count()
