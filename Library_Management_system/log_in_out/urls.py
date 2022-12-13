from django.urls import path
from .views import sign_up, sign_in, logoutt
urlpatterns = [
    path("", sign_in, name="signin"),
    path("signup/", sign_up, name="signup"),
    path("logout", logoutt, name="logout"),
]
