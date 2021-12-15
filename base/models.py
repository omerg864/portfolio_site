from os import link
from django.db import models

# Create your models here.

class Bio(models.Model):
    f_name = models.CharField(max_length=100)
    l_name = models.CharField(max_length=100)
    he_f_name = models.CharField(max_length=100)
    he_l_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    he_address = models.CharField(max_length=100)
    introduction = models.TextField(blank=True)
    he_introduction = models.TextField(blank=True)
    he_cv = models.CharField(max_length=300)
    en_cv = models.CharField(max_length=300)
    git_hub = models.CharField(max_length=300)
    linked_in = models.CharField(max_length=300)
    facebook = models.CharField(max_length=300)
    instagram = models.CharField(max_length=300)
    twitter = models.CharField(max_length=300)
    short_intro = models.TextField(blank=True)
    he_short_intro = models.TextField(blank=True)
    photo = models.CharField(max_length=300)
    exp_years = models.IntegerField()
    num_projects = models.IntegerField()
    num_works = models.IntegerField()

class Title(models.Model):
    title_en = models.CharField(max_length=100)
    title_he = models.CharField(max_length=100)

class Skill(models.Model):
    skill_en = models.CharField(max_length=30)
    photo = models.CharField(max_length=300)
    info = models.CharField(max_length=30)

class Education(models.Model):
    year = models.DateField(blank=False)
    title = models.CharField(max_length=100)
    sub_title = models.CharField(max_length=200, blank=True)
    info = models.TextField(blank=True)
    link = models.CharField(max_length=300, blank=True)

class Experience(models.Model):
    year = models.DateField(blank=False)
    title = models.CharField(max_length=100)
    sub_title = models.CharField(max_length=200, blank=True)
    info = models.TextField(blank=True)
    link = models.CharField(max_length=300, blank=True)

class Project(models.Model):
    date = models.DateField(blank=False)
    title = models.CharField(max_length=100)
    info = models.TextField(blank=True)
    photo = models.CharField(max_length=300)
