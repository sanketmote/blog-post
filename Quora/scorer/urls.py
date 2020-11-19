from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from . import views

urlpatterns = [
    path('Register', views.Register.as_view(), name="Register"),
]
