from django import forms
from django.db import models
from .models import Question, Choice

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['question_text']

class ChoiceForm(forms.ModelForm):
    class Meta:
        model = Choice
        fields = ['question_id', 'votes', 'choice_text']
