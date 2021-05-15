from django.shortcuts import render, redirect

from app.models.user import User
from django.contrib.auth.hashers import check_password
from django.views import View

class Logout(View):
    def get(self, request):
        request.session.clear()
        return redirect('login')
    def post(self, request):
        pass