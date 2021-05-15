from django.shortcuts import render, redirect
from django.contrib import messages
from app.models.user import User
from django.contrib.auth.hashers import make_password
from django.views import View


class Signup(View):
    def get(self, request):
        return render(request, 'signup.html')

    def post(self, request):
        postData = request.POST
        first_name = postData.get('first_name')
        last_name = postData.get('last_name')
        email = postData.get('email')
        password = postData.get('password')

        # validation
        value = {
            'first_name': first_name,
            'last_name': last_name,
            'email': email
        }
        error_message = None

        user = User(first_name=first_name,
                            last_name=last_name,
                            email=email,
                            password=password)

        error_message = self.validationUser(user)

        if not error_message:
            print(postData, first_name, last_name, email, password)

            user.password = make_password(user.password)
            user.register()
            messages.success(request, 'Registered Successfully, Please login.')
            return redirect('/')
        else:
            data = {
                'error': error_message,
                'values': value
            }
            return render(request, 'signup.html', data)
            # return redirect('homepage')

    def validationUser(self, user):
        error_message = None
        errors = []

        if (not user.first_name):
            errors.append("First name is Required !!")
        elif len(user.first_name) < 4:
            errors.append("First Name must be 4 char long or more ")

        if not user.last_name:
            errors.append("Last Name Is Required")
        elif len(user.last_name) < 4:
            errors.append("Last Name must be 4 char long or more")

        if not user.password:
            errors.append("Password is Required")
        elif len(user.password)<6 :
            errors.append("Password must be 6 char long")

        if not user.email:
            errors.append("Email must be Required")

        if user.isExists():
            # error_message = "Email Address Already Registered.."
            errors.append("Email Address Already Registered..")
        return errors

