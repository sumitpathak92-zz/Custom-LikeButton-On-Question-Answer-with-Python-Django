'''
Created on 11-Sep-2015

@author: sumit
'''
from django.conf.urls import url
from . import views

urlpatterns = [
              url(r'^$', views.index, name='index'),
              url(r'^(?P<question_id>[0-9]+)/details/$', views.details, name='details'),
              url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
              url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
              url(r'^buttons/page(?P<question_id>[0-9]+)/$', views.page, name = 'page'),
              ]
