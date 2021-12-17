from django.shortcuts import render
from .models import Bio, Title, Skill, Education, Experience, Project
from django.template.defaulttags import register
from portfolio.settings import EMAIL_HOST_USER
from django.core.mail import send_mail
import json


def base(request):
    bio = Bio.objects.all().first()
    titles = Title.objects.order_by("num")
    titles_en = []
    titles_he = []
    for title in titles:
        titles_en.append(title.title_en)
        titles_he.append(title.title_he)
    skills = Skill.objects.order_by("num")
    educations = Education.objects.order_by("-year")
    experiences = Experience.objects.order_by("-year")
    projects = Project.objects.order_by("-date")
    context = {
        'bio': bio,
        'titles_en': json.dumps(titles_en),
        'titles_he': json.dumps(titles_he),
        'skills': skills,
        'educations': educations,
        'experiences': experiences,
        'projects': projects,
    }
    if request.method == 'POST':
        if 'message' in request.POST:
            message = request.POST.get('message')
            name = request.POST.get('message-name')
            email = request.POST.get('message-email')
            subject = request.POST.get('message-subject')
            sent = send_mail(subject, f'name: {name}\nEmail: {email}\n{message}', EMAIL_HOST_USER, [bio.email], fail_silently=False)
            if sent == 1:
                context["message"] = "Message sent successfully!"
            else:
                context["message"] = "Error: Message did not send!"
            return render(request, "index.html", context)
    return render(request, "index.html", context)


@register.filter
def num_string(num):
    if num < 10 and num != 0:
        return "0" + str(num)
    return str(num)
