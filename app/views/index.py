from django.shortcuts import render, redirect

from app.models.user import User
from django.contrib.auth.hashers import make_password
from django.views import View


class Index(View):
    def get(self, request):
        return render(request, 'home.html')