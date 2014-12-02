from django.shortcuts import render
from django.http import HttpResponse
from polls.models import Question
from django.template import RequestContext , loader
from django.http import Http404
from django.shortcuts import get_object_or_404, render
# Create your views here.




def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)    
    

def detail(request,question_id):
   
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})


def results(request,question_id):
    reponse = "result of question number %s" 
    return HttpResponse(response %question_id)

def vote(request,question_id):
    return HttpResponse("Voting on quesiton %s" %question_id)
