from django.urls import path
from authapp import views

urlpatterns = [
   path('', views.Home, name="Home"),
   path('signup', views.signup, name="signup"),
   path('login', views.handle_login, name="handle_login"),
   path('logout', views.handle_logout, name="handle_logout"),
   path('contact', views.contact, name="contact"),
   path('join', views.enroll, name="enroll"),
   path('profile', views.profile, name="profile"),
   path('attendance',views.attendance,name="attendance"),
    path('gallery',views.gallery,name="gallery")
]