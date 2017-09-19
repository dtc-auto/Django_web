#coding=utf-8
from django.db import models


class MAP(models.Model):


    W_Brand = models.CharField(max_length=100)
    W_City = models.CharField(max_length=100)
    R_City = models.CharField(max_length=100)
    R_Province = models.CharField(max_length=100)
    R_Region = models.CharField(max_length=100)
    M_province_pinyin = models.CharField(max_length=100)
    M_province = models.CharField(max_length=100)


class LEVEL1(models.Model):

    score = models.CharField(max_length=100)
    Aspect = models.CharField(max_length=100)
    Brand = models.CharField(max_length=100)


class LEVEL2(models.Model):

    Brand = models.CharField(max_length=100)
    Dimension = models.CharField(max_length=100)
    keyindex = models.CharField(max_length=100)
    KeyModifier = models.CharField(max_length=100)
    SentenceAttitude = models.CharField(max_length=100)
    Case = models.CharField(max_length=100, default='')

class PURPOSE(models.Model):

    ForChild = models.CharField(max_length=100)
    ForWork = models.CharField(max_length=100)
    ForShopping = models.CharField(max_length=100)
    ForBusiness = models.CharField(max_length=100)
    ForCrossCountry = models.CharField(max_length=100)
    ForLongDistance = models.CharField(max_length=100)
    ForRacing = models.CharField(max_length=100)
    ForSelfDriving = models.CharField(max_length=100)
    ForCarry = models.CharField(max_length=100)
    ForGirls = models.CharField(max_length=100)
    Brand = models.CharField(max_length=100)