from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=40)
    gender = models.CharField(max_length=100)
    dob = models.CharField(max_length=100)
    age = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    pin_code = models.CharField(max_length=100)
    mobile_number = models.CharField(max_length=100)

    def register(self):
        self.save()

    @staticmethod
    def get_user_by_email(email):
        try:
            return User.objects.get(email=email)
        except:
            return False

    def isExists(self):
        if User.objects.filter(email=self.email):
            return True
        return False




