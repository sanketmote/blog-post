from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth, Group
from django.template.response import TemplateResponse
from django.urls import reverse
from .models import *
from django.http import *
from django.views import View

class Register(View):

    def get(self, request, template_name='register.html'):
        return render(request, template_name)