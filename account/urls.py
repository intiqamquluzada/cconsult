from django.urls import path
from account.views import *


urlpatterns = [

    path("register/", register_view, name='register'),
    path("otp/<slug>/", otp_view, name='otp'),

]