from django.shortcuts import render
from .models import Bio, Title, Skill, Education, Experience, Project
from django.template.defaulttags import register

def base(request):
    bio = Bio.objects.all().first()
    titles = Title.objects.all()
    skills = Skill.objects.all()
    educations = Education.objects.all()
    experiences = Experience.objects.all()
    projects = Project.objects.all()
    context = {
        'bio': bio,
        'titles': titles,
        'skills': skills,
        'educations': educations,
        'experiences': experiences,
        'projects': projects,
    }
    return render(request, "index.html", context)


@register.filter
def num_string(num):
    if num < 10:
        return "0" + str(num)
    return str(num)
