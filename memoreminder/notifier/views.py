from django.shortcuts import render
from .models import Notification
from django.utils import timezone
from django.shortcuts import HttpResponse
# Create your views here.

def b_day_list(request):
    today = timezone.now()
    print(today.month)
    print(today.day)
    people = Notification.objects.filter(Date__day = today.day , Date__month=today.month)
    reply=""
    for person in people:
        reply+="its " + str(person.Name) +"'s "+str(person.Occasion) +" today\n"
    return HttpResponse(reply)