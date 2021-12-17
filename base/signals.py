from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Skill, Title


@receiver(post_save, sender=Skill)
def send_number_served(sender, instance, created, **kwargs):
    if len(Skill.objects.filter(num=instance.num)) > 1:
        skills = Skill.objects.filter(num__gte=instance.num)
        temp = instance.num
        for skill in skills:
            if skill.skill_en != instance.skill_en:
                skill.num = instance.num + 1
                skill.save()
                instance.num += 1


@receiver(post_save, sender=Title)
def send_number_served(sender, instance, created, **kwargs):
    if len(Title.objects.filter(num=instance.num)) > 1:
        skills = Title.objects.filter(num__gte=instance.num)
        temp = instance.num
        for skill in skills:
            if skill.title_en != instance.title_en:
                skill.num = instance.num + 1
                skill.save()
                instance.num += 1
