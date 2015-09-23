from django.shortcuts import render
from django.http import HttpResponse, Http404 

from django.template import Template, Context 
import datetime
from django.template.loader import get_template
# Create your views here.

def hello(request):#request object contains info about the current web request that triggered this view
    return HttpResponse("hello sumit") #http respopnse object that is instantiated with text "hello sumit"

def view_tweet(request):
    return HttpResponse("default view for tweet page")

def like(request):
    return HttpResponse("this is the response object for like button")

def homepage_view(request):
    return HttpResponse("welcome to the homepage for tis site")

def server_time(request):
    timenow = datetime.datetime.now()
    t = get_template('current_datetime.html')
    html = t.render(Context({'current_time' : timenow}))
    return HttpResponse(html)

def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours = offset)
    html = "<html><body>In %s hour(s), it will be %s.</body></html>" % (offset, dt)
    return HttpResponse(html)
