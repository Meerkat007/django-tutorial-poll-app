from django.db import models

# The single, definitive source of truth about my data.
# Contains the essential fields and behaviors of the data I'm storing

#class subclass models.Model
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
