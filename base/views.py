from django.shortcuts import render
from .models import Bio, Title, Skill, Education, Experience, Project


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
