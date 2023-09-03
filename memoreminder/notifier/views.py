from django.shortcuts import render
from .models import Notification
from django.utils import timezone
from django.shortcuts import HttpResponse
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.

def notify():
    today = timezone.now()
    people = Notification.objects.filter(Date__day = today.day , Date__month=today.month)
    if people:
        for person in people:
            sub="REMINDER \U0001F4A5 \U0001F49D \U0001F60A"
            msg ="Its " + str(person.Name) + "'s " + str(person.Occasion)+ " today. Remember to wish them."
            send_mail(sub, msg, settings.EMAIL_HOST_USER,["negiaryan53@gmail.com"],fail_silently=False)
        print("snd")
    else:
        pass


def b_day_list(request):
    today = timezone.now()
    people = Notification.objects.filter(Date__day = today.day , Date__month=today.month)
    reply=""
    for person in people:
        reply+="its " + str(person.Name) +"'s "+str(person.Occasion) +" today"

    return HttpResponse(str(today.hour)+str(today.minute)+reply)