# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django import forms
from models import User
from autohome_pages.Connect_DB import getCarOwner, getColumnChart_p1, getLevel1Attributes, getLevel2Attributes, getPurpose
import json

class UserForm(forms.Form):
    username = forms.CharField(label='username', max_length=50)
    password = forms.CharField(label='password', widget=forms.PasswordInput())


def login(request):
    if request.method == 'POST':
        userform = UserForm(request.POST)
        if userform.is_valid():
            username = userform.cleaned_data['username']
            password = userform.cleaned_data['password']

            user = User.objects.filter(username__exact=username, password__exact=password)

            if user:
                return render_to_response('index.html',
                                          {'userform': userform},
                                          context_instance=RequestContext(request))
            else:
                return HttpResponse('wrong username or password, please re-input')
    else:
        userform = UserForm()
    return render_to_response('login.html',
                              {'userform': userform},
                              context_instance=RequestContext(request))

def base(request):
    return render(request, 'index.html')

def dashboard(request):
    return render(request, 'dashboard.html')

def carOwnerChartPage(request):
    return render(request, 'regionDistribution.html')

def level1ChartPage(request):
    return render(request, 'level1.html')

def level2ChartPage(request):
    return render(request, 'level2.html')

def purposeChartPage(request):
    return render(request, 'purpose.html')

def carOwnerChart(request):
    target = request.GET.get('a','')
    list1 = getCarOwner(target)
    list2 = getColumnChart_p1()
    dict = {'list1': list1,'list2':list2}
    return HttpResponse(json.dumps(dict), content_type='application/json')

def level1chart(request):
    target = request.GET.get('a','')
    list1 = getLevel1Attributes(target)
    dict = {'list1': list1}
    return HttpResponse(json.dumps(dict), content_type='application/json')

def level2chart(request):
    target = request.GET.get('a','')
    list1 = getLevel2Attributes(target)
    dict = {'list1': list1}
    return HttpResponse(json.dumps(dict), content_type='application/json')

def purposeChart(request):
    target = request.GET.get('a','')
    list1 = getPurpose(target)
    dict = {'list1': list1}
    return HttpResponse(json.dumps(dict), content_type='application/json')
