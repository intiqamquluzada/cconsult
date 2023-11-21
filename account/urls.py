from django.urls import path
from account.views import *

urlpatterns = [

    path("register/", register_view, name='register'),
    path("otp/<slug>/", otp_view, name='otp'),
    path("email/", email_view, name='email'),
    path("forgot/check/<slug>/", forgot_checker, name='forgot_otp'),
    path("reset/password/<slug>/", reset_password, name='reset_password'),

]
