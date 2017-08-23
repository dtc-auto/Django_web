# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render
import pymssql
import pandas as pd
import json
from Connect_DB import getCarOwner,getColumnChart_p1,getLevel1Attributes,getLevel2Attributes,getPurpose


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
