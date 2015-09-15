from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Question
from buttonapp.models import Choice
from django.http.response import HttpResponseRedirect
from django.core.urlresolvers import reverse

# Create your views here.

# each view is responsible for doing one of the two things, returning an HttpResponse object containing the content for
# the requested page, or raising an exception such as Http404
def index(request):
    latest_ques_list = Question.objects.order_by('pub_date')[:5]
    context = {'latest_question_list' : latest_ques_list}
    return render(request, 'buttonapp/index.html', context)

def details(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    # get_object_or_404 takes a DJANGO MODEL as its first argument and an arbitrary no of keyword arguments which
    # it pases to the get() function of the model's manager.Raises http404 if object doesn't exist
    return render(request, 'buttonapp/details.html', {'question' : question}) 

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'buttonapp/results.html', {'question' : question})

def vote(request, question_id):
    p = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except(KeyError, Choice.DoesNotExist):
        # redisplay the question voting form 
        return render(request, 'buttonapp/details.html', {
                                                          'question' : p,
                                                          'error_message' : "you did not select any choice",
                                                          })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('buttonapp:results', args=(p.id,)))        

def page(request, num='1'):
    return HttpResponse("you are watching the page number %s" % num)
