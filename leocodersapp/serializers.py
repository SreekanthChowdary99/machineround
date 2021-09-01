from django.db import models
from rest_framework import fields, serializers
from .models import User,Schedule
from django.contrib.auth.password_validation import validate_password
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User,Schedule
from datetime import date


from django import forms
from datetimewidget.widgets import DateTimeWidget
import datetime

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields='__all__'

class DateInput(forms.DateInput):
    input_type = 'date'

class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model=Schedule
        fields='__all__'
    def validate(self, data):
        print(data)
        print(type(data['date']))
        if data['date'] < data['date'].today():
            raise serializers.ValidationError("Date should be upcoming")
        if data['date'].weekday() >=5:
            raise serializers.ValidationError("Date should not be in weekends")
        return data