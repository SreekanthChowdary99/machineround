from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from leocodersapp.views import home_view, signup_view,Login,AppointmentViewSet,SignupViewset
from django.contrib.auth import logout, views as auth
from rest_framework import routers
from leocodersapp import views
from django.urls import path, include
import rest_framework
from rest_framework import routers

router = routers.DefaultRouter()
router.register('schedule', AppointmentViewSet)
router.register('signupview', SignupViewset)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name="home"),
    path('signup/', signup_view, name="signup"),
    path('login/', Login, name ='login'),
    path('api/', include(router.urls)),
]