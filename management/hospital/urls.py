# urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register',views.register,name="register"),
    path('login',views.login_page,name="login"),
    path('login_out',views.loginout_page,name="login_out"),
    path('about',views.about,name='about'),
    path('appointment',views.appointment,name='appointment'),
    path('confirmation',views.confiramation,name="confiramtion"),
    path('appointment_list',views.appointment_list,name='appointment_list'),
    path('doctors',views.doctors_views,name='doctors'),
    path('contact',views.contact,name='contact'),
    path('contactconf',views.contactconf,name='contactconf'),
    path('booking/<int:booking_id>/edit/', views.edit_booking, name='edit_booking'),
    path('appointments/<int:booking_id>/delete/', views.delete_appointment, name='delete_appointment'),
    path('dashboard',views.dashboard_doctor,name='dashboard'),
    path('doctor_app',views.appointment_app,name='doctors_app'),
    path('doctors_list/<int:doctor_id>/appointments/', views.doctor_appointments, name='doctor_appointments'),
    path('feedback',views.feed_back,name="feedback"),
    path('feedconf',views.feedconf,name='feedconf'),
    path('feature',views.features,name="feature")
    
   
    
  

]
