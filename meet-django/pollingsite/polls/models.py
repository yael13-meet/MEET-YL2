from django.db import models

# Create your models(classes) here.
class Ques(models.Model):
	text=models.CharField(max_length=200)

class Option(models.Model):
	text=models.CharField(max_length=200)
	numVote=models.IntegerField()
	x=models.ForeignKey(Ques)
