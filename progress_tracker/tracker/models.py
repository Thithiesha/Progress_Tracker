from django.db import models
from django.contrib.auth.models import User

class Subject(models.Model):
    subject_name = models.CharField(max_length=100)

    def __str__(self):
        return self.subject_name

class ExamScore(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    score = models.FloatField()
    date_of_exam = models.DateField()

    def __str__(self):
        return f"{self.user.username} - {self.subject.subject_name} - {self.score}"
