from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("First view")

def detail(request,question_id):
    return HttpResponse("Question Number %s" %question_id)

def results(request,question_id):
    reponse = "result of question number %s" 
    return HttpResponse(response %question_id)

def vote(request,question_id):
    return HttpResponse("Voting on quesiton %s" %question_id)
