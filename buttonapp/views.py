from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader 
from .models import Question
from django.template.context import RequestContext
# Create your views here.

# each view is responsible for doing one of the two things, returning an HttpResponse object containing the content for
#the requested page, or raising an exception such as Http404
def index(request):
    latest_ques_list = Question.objects.order_by('-pub_date')[:2]
    template = loader.get_template('buttonapp/index.html')
    context = RequestContext(request, {
                                       'latest_question_list' : latest_ques_list
                                       })
    return HttpResponse(template.render(context))

def details(request, question_id):
    return HttpResponse("you are looking at question %s" % question_id)

def results(request, question_id):
    response = "You are watching the results of question %s"
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You are voting on question %s" % question_id)

def page(request, num = '1'):
    return HttpResponse("you are watching the page number %s" % num)

