from django.contrib import admin

# Register your models here.
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .models import User,Schedule
from django.contrib.auth.forms import UserChangeForm

admin.site.register(Schedule)