from __future__ import unicode_literals
from django.contrib import admin
from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    email = models.EmailField()


class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'password')


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


class User(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    email = models.EmailField()


class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'password')


admin.site.register(User, UserAdmin)