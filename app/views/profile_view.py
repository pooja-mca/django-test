from django.shortcuts import render, redirect

from app.models.user import User
from django.contrib.auth.hashers import make_password
from django.views import View


class Profile_view(View):
    def get(self, request):
        user=User.objects.get(id=request.session.get('user'))
        return render(request, 'profile_view.html',{'user':user})