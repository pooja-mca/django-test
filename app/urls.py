from django.contrib import admin
from django.urls import path
# from.import views
from .views import signup,index,login,logout,profile,profile_view

urlpatterns = [
    path('', index.Index.as_view(),name='index'),
    path('signup', signup.Signup.as_view(),name='signup'),
    path('login', login.Login.as_view(),name='login'),
    path('logout', logout.Logout.as_view(),name='logout'),
    path('profile', profile.Profile.as_view(),name='profile'),
    path('update_profile', profile.Profile.as_view(),name='profile'),
    path('profile_view', profile_view.Profile_view.as_view(),name='profile_view'),

]