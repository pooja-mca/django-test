from django.shortcuts import render, redirect
from django.contrib import messages

from django.views import View
from app.models.user import User


class Profile(View):
    def get(self, request):
        user= User.objects.get(id=request.session.get('user'))
        return render(request, 'profile.html',{'user':user })

    def post(self,request):
        postData = request.POST
        first_name = postData.get('first_name')
        last_name = postData.get('last_name')
        email = postData.get('email')
        dob = postData.get('dob')
        gender = postData.get('gender')
        age = postData.get('age')
        address = postData.get('address')
        city = postData.get('city')
        state = postData.get('state')
        country = postData.get('country')
        pin_code = postData.get('pin_code')
        mobile_number = postData.get('mobile_number')

        value = {
            'first_name': first_name,
            'last_name': last_name,
            'email': email,
            'dob':dob,
            'gender':gender,
            'age':age,
            'address':address,
            'city':city,
            'state':state,
            'country':country,
            'pin_code':pin_code,
            'mobile_number':mobile_number
        }
        error_message = None
        user=User.objects.filter(id=request.session.get('user')).update(first_name=first_name,
                    last_name=last_name,
                    email=email,
                    dob= dob,
                    gender=gender,
                    age= age,
                    address= address,
                    city=city,
                    state=state,
                    country=country,
                    pin_code= pin_code,
                    mobile_number=mobile_number
        )
        if user:
            messages.success(request, 'Profile Updated successfully.')
        return redirect('/profile')



