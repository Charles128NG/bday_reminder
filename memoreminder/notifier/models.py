from django.db import models

# Create your models here.
class Notification(models.Model):
    Name = models.CharField(max_length=150)
    Occasion = models.CharField(max_length=100)
    Date = models.DateField()#mm-dd

    def __str__(self):
        return self.Name
