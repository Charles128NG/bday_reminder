from django.core.management.base import BaseCommand
from django.core.mail import send_mail
from django.utils import timezone
from notifier.models import Notification
from django.conf import settings
class Command(BaseCommand):
    help = 'Send emails to users'

    def handle(self, *args, **kwargs):
        today = timezone.now()
        try:
            people = Notification.objects.filter(Date__day = today.day , Date__month=today.month)
            if people:
                for person in people:
                    sub="REMINDER \U0001F4A5 \U0001F49D \U0001F60A"
                    msg ="Its " + str(person.Name) + "'s " + str(person.Occasion)+ " today. Remember to wish them."
                    send_mail(sub, msg, settings.EMAIL_HOST_USER,["negiaryan53@gmail.com"],fail_silently=False)
                    self.stdout.write(self.style.SUCCESS(f'Successfully sent email to {person.Name}'))
            else:
                self.stdout.write(self.style.SUCCESS(f'no one to send email'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'{str(e)}'))