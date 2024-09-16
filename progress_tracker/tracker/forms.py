from django import forms
from .models import ExamScore

class ExamScoreForm(forms.ModelForm):
    class Meta:
        model = ExamScore
        fields = ['subject', 'score', 'date_of_exam']
