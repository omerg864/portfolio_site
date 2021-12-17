from django.shortcuts import render
from .models import Bio, Title, Skill, Education, Experience, Project
from django.template.defaulttags import register
from portfolio.settings import EMAIL_HOST_USER
from django.core.mail import send_mail


def base(request):
    bio = Bio.objects.all().first()
    titles = Title.objects.all()
    skills = Skill.objects.all()
    educations = Education.objects.all()
    experiences = Experience.objects.all()
    projects = Project.objects.all()
    if request.method == 'POST':
        if 'message' in request.POST:
            message = request.POST.get('message')
            print(message)
            name = request.POST.get('message-name')
            email = request.POST.get('message-email')
            subject = request.POST.get('message-subject')
            print(EMAIL_HOST_USER)
            print(bio.email)
            send_mail(subject, f'{name}\n{email}\n{message}', EMAIL_HOST_USER, [bio.email], fail_silently=False)
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
    if num < 10 and num != 0:
        return "0" + str(num)
    return str(num)
