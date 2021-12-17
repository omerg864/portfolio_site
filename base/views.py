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
    educations = make_three(Education.objects.order_by("-year"))
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

def make_three(queryset):
    newlist = []
    added_num = 1
    if len(queryset) % 3 == 0:
        added_num = 0
    for i in range(int(len(queryset) / 3) + added_num):
        newlist.append({"year1": "", "year2": "", "year3": "", "title1": "", "title2": "", "title3": "", "sub_title1": "", "sub_title2": "", "sub_title3": "", "info1": "", "info2": "", "info3": "", "link1": "", "link2": "", "link3": ""})
    index = 0
    index2 = 1
    for item in queryset:
        print(item)
        newlist[index]["year" + str(index2)] = item.year
        newlist[index][f"title{index2}"] = item.title
        newlist[index][f"sub_title{index2}"] = item.sub_title
        newlist[index][f"info{index2}"] = item.info
        newlist[index][f"link{index2}"] = item.link
        if i % 2 == 0 and i != 0:
            index += 1
            index2 = 1
        index2 += 1
    print(newlist)
    return newlist


@register.filter
def num_string(num):
    if num < 10 and num != 0:
        return "0" + str(num)
    return str(num)

@register.filter
def is_reminder(num):
    return num % 2 == 0
