from django.contrib import admin
from .models import Department, Booking, Doctor,Contact,Feedback
from django.contrib import admin


admin.site.register(Department)

class BookingAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'phone', 'booked', 'time', 'desc')

admin.site.register(Booking, BookingAdmin)

class DoctorAdmin(admin.ModelAdmin):
    list_display = ('doc_name', 'doc_dep', 'doc_image')

admin.site.register(Doctor, DoctorAdmin)


class contactAdmin(admin.ModelAdmin):
    list_display=('name','email','subject','message')

admin.site.register(Contact,contactAdmin)    


class FeedbackAdmin(admin.ModelAdmin):
    list_display=('name','email','message')

admin.site.register(Feedback,FeedbackAdmin)    





