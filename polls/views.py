from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Question

# Create your views here.

class AnswerSurveys(TemplateView):
    template_name = 'answer_survey.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["questions"] = Question.objects.all() 
        return context

class Home(TemplateView):
    template_name = 'responses.html'

    
