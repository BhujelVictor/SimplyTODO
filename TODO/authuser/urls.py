from django.urls import path
from .views import Homepage, Register, Login, Logoutuser, test

urlpatterns = [
   path('',Homepage, name="home-page"),
   path('register/',Register, name="register-page"),
   path('login/',Login, name="login-page"),
   path('loginout/',Logoutuser, name="logout-page"),
   path('test/',test, name="test-page"),
]
