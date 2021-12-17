from django.db import models

# Create your models here.

class Bio(models.Model):
    f_name = models.CharField(max_length=100)
    l_name = models.CharField(max_length=100)
    he_f_name = models.CharField(max_length=100, blank=True)
    he_l_name = models.CharField(max_length=100, blank=True)
    email = models.EmailField(max_length=100, blank=True)
    phone = models.CharField(max_length=100, blank=True)
    address = models.CharField(max_length=100, blank=True)
    he_address = models.CharField(max_length=100, blank=True)
    introduction = models.TextField(blank=True)
    he_introduction = models.TextField(blank=True)
    he_cv = models.CharField(max_length=300, blank=True)
    en_cv = models.CharField(max_length=300, blank=True)
    git_hub = models.CharField(max_length=300, blank=True)
    linked_in = models.CharField(max_length=300, blank=True)
    facebook = models.CharField(max_length=300, blank=True)
    instagram = models.CharField(max_length=300, blank=True)
    twitter = models.CharField(max_length=300, blank=True)
    short_intro = models.TextField(blank=True)
    he_short_intro = models.TextField(blank=True)
    photo = models.CharField(max_length=300, blank=True)
    exp_years = models.IntegerField(default=0)
    num_projects = models.IntegerField(default=0)
    num_works = models.IntegerField(default=0)
    title = models.CharField(max_length=30, blank=True)

    def __str__(self):
        return self.f_name + " " + self.l_name

class Title(models.Model):
    title_en = models.CharField(max_length=100)
    title_he = models.CharField(max_length=100, blank=True)
    num = models.IntegerField(default=0)

    def __str__(self):
        return self.title_en

class Skill(models.Model):
    skill_en = models.CharField(max_length=30)
    photo = models.CharField(max_length=300, blank=True)
    info = models.CharField(max_length=30, blank=True)
    num = models.IntegerField(default=0)

    def __str__(self):
        return self.skill_en

class Education(models.Model):
    year = models.DateField()
    title = models.CharField(max_length=100)
    sub_title = models.CharField(max_length=200, blank=True)
    info = models.TextField(blank=True)
    link = models.CharField(max_length=300, blank=True)

    def __str__(self):
        return self.title

class Experience(models.Model):
    year = models.DateField()
    title = models.CharField(max_length=100)
    sub_title = models.CharField(max_length=200, blank=True)
    info = models.TextField(blank=True)
    link = models.CharField(max_length=300, blank=True)

    def __str__(self):
        return self.title

class Project(models.Model):
    date = models.DateField()
    title = models.CharField(max_length=100)
    info = models.TextField(blank=True)
    photo = models.CharField(max_length=300, blank=True)
    link = models.CharField(max_length=500, blank=True)
    action = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.title
