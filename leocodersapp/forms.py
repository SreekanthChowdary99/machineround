from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User,Schedule
from datetime import date

from django import forms
from datetimewidget.widgets import DateTimeWidget
import datetime

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=100, help_text='Last Name')
    last_name = forms.CharField(max_length=100, help_text='Last Name')
    email = forms.EmailField(max_length=150, help_text='Email')
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

class DateInput(forms.DateInput):
    input_type = 'date'
    
class ScheduleForm(forms.ModelForm):

    class Meta:
        model = Schedule
        fields = ('date', 'timeslot', 'name')
        widgets = {
             'date': DateInput(
                    format=('%Y-%m-%d'),
                    attrs={
                    'minView': 2,
                    'maxView': 3,
                    'weekStart': 1,
                    'todayHighlight': True,
                    'format': 'yyyy-mm-dd',
                    'daysOfWeekDisabled': [0, 6],
                    'startDate': date.today().strftime('%Y-%m-%d'),
                    }

             ),
        }

    def clean_date(self,attrs=None, renderer=None):
        day = self.cleaned_data['date']
        print(day)
        if day <= date.today():
            raise forms.ValidationError('Date should be upcoming', code='invalid')
            
        if day.weekday() >=5:
            raise forms.ValidationError('Date should be a weekend', code='invalid')

        return day
