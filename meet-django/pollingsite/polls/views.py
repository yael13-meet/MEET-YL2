from django.shortcuts import render
from django.http import HttpResponse

from models import Ques, Option

def add(request,x,y):
	return HttpResponse(int(x)+int(y))

def hi(request):
	return render(request, "polls/page about me.html")

def contact(request):
	return render(request, "polls/contact me.html")

def polls(request):
	listQues=Ques.objects.all()
	return render(request, "polls/polls.html", {"listQues":listQues})


# Create your views(functions) here.
# Remember each function/view the first argument/input has to be request