from django.shortcuts import render
from django.http import HttpResponse, Http404 
import datetime
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
    return render(request, 'current_datetime.html', {'current_time': timenow})

def hours_ahead(request, offset):
    offset = int(offset)
    dt = datetime.datetime.now() + datetime.timedelta(hours = offset)
    return render(request, 'hours_ahead.html', {'hour_offset' : offset, 'next_time' : dt})
