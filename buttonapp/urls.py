'''
Created on 11-Sep-2015

@author: sumit
'''
from django.conf.urls import url
from . import views

urlpatterns= [
              url(r'^$', views.index, name='index'),
              url(r'^$', views.index, name = 'index2'),
              ]