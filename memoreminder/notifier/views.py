from django.shortcuts import render
from .models import Notification
from django.utils import timezone
from django.shortcuts import HttpResponse
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.

def b_day_list(request):
    today = timezone.now()
    people = Notification.objects.filter(Date__day = today.day , Date__month=today.month)
    reply=""
    for person in people:
        reply+="its " + str(person.Name) +"'s "+str(person.Occasion) +" today"

    return HttpResponse(str(today.hour)+str(today.minute)+reply)
