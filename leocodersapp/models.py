from re import T
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from datetime import date
import datetime
from AppointmentProject import settings

class User(AbstractUser):
   username = models.CharField(max_length = 50, blank = True, null = True, unique = True)
   email = models.EmailField(_('email address'), unique = True)
   native_name = models.CharField(max_length = 5)
   phone_no = models.CharField(max_length = 10)
   USERNAME_FIELD = 'email'
   REQUIRED_FIELDS = ['username', 'first_name', 'last_name']
   def __str__(self):
       return "{}".format(self.email)

class Schedule(models.Model):

    class Meta:
        unique_together = ('date', 'timeslot','name')

    TIMESLOT_LIST = (
        (0, '09:00 – 10:00'),
        (1, '10:00 – 11:00'),
        (2, '11:00 – 12:00'),
        (3, '12:00 – 13:00'),
        (4, '13:00 – 14:00'),
        (5, '14:00 – 15:00'),
        (6, '15:00 – 16:00'),
        (7, '16:00 – 17:00'),
        (8, '17:00 – 18:00'),
    )

    date = models.DateField(_("Date"), default=datetime.date.today,help_text="YYYY-MM-DD")
    timeslot = models.IntegerField(choices=TIMESLOT_LIST,default=None)
    name = models.CharField(max_length=60,default=None)
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)

    # def __str__(self):
    #     return '{} {} {}. user: {}'.format(self.date, self.time, self.name)

    # @property
    # def time(self):
    #     return self.TIMESLOT_LIST[self.timeslot][1]

class OutCsv(models.Model):
    code=models.IntegerField()
    symbole=models.CharField(max_length = 10)
    date=models.DateField(blank=True,null=True)
    open=models.FloatField()
    high=models.FloatField()
    low=models.FloatField()
    close=models.FloatField()
    volume=models.FloatField()
    adjclose=models.FloatField()
