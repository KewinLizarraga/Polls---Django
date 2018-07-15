import datetime

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils import timezone

# Create your models here.

@python_2_unicode_compatible	# only if you need to support Python2
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pud_date = models.DateTimeField('date published')
    
    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

@python_2_unicode_compatible	# only if you need to support Python2
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choise_text
