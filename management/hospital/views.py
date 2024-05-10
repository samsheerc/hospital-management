
from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms import BookingForm,ContactForm,FeedbackForm
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import UserRegistrationForm
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout
from .models import Doctor
from django.shortcuts import render, get_object_or_404
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .models import Doctor,Contact

def register(request):
    form=UserRegistrationForm()
    if request.method=='POST':
       form=UserRegistrationForm(request.POST)
       if form.is_valid():
          form.save()
          messages.success(request,"Registration sucess you can login now..!")
          return redirect("login")
    return render(request,"register.html",{'form':form})


def loginout_page(request):
   if request.user.is_authenticated:
      logout(request)
      messages.success(request,"Logged out successfully")
      return redirect("/")


def login_page(request):
    if request.user.is_authenticated:
        return redirect('login')
    else:
        if request.method == 'POST': 
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)  
            if user is not None:
                login(request, user)
                # Redirect the user to the home page or another appropriate page
                return redirect("/")
            else:
                # Display a more specific error message
                messages.error(request, "Invalid username or password. Please try again.")
                return redirect("/login")
    return render(request, "login.html")


def index(request):
    department=Department.objects.all()
    doctor=Doctor.objects.all()
    form=BookingForm()
    context={
        "department": department,
        "doctor": doctor,
        "form": form,
    }
    if request.method=="POST":
        form=BookingForm(request.POST)
        if form.is_valid():
            form.save()
            form=BookingForm()
            return render(request,"index.html",context)
    return render(request, "index.html",context)


def about(request):
    return render(request,'about.html')

def appointment(request):
    if not request.user.is_authenticated:
        messages.info(request, "Please log in to make an appointment.")
        return redirect('login')  # Assuming 'login' is the name of your login URL
    else:
        department = Department.objects.all()
        doctor = Doctor.objects.all()
        form = BookingForm()
        context = {
            "department": department,
            "doctor": doctor,
            "form": form,
        }
        if request.method == "POST":
            form = BookingForm(request.POST)
            if form.is_valid():
                form.save()
                form = BookingForm()
                messages.success(request, "Appointment booked successfully!")
                return render(request, "inc/confirmation.html", context)
        return render(request, 'appointment.html', context)


def confiramation(request):
    return render(request,'confirmation.html')

def contactconf(request):
    return render(request,'contactconf.html')



def appointment_list(request):
    appointments = Booking.objects.all()
    return render(request, 'appointlist.html', {'appointments': appointments})

def edit_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    
    if request.method == 'POST':
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            return redirect('appointment_detail', booking_id=booking_id)  # Redirect to booking detail page
    else:
        form = BookingForm(instance=booking)
    
    return render(request, 'edit_appointment.html', {'form': form})


def delete_appointment(request, pk):
    appointment = Booking.objects.get(pk=pk)
    appointment.delete()
    appointments = Booking.objects.all()  
    return render(request, 'appointlist.html', {'appointment': appointments})




        






def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your message has been sent successfully!")
            return redirect('contactconf')  # Redirect to confirmation page
    else:
        form = ContactForm()
    
    return render(request, "contact.html", {"form": form})





def doctors_views(request):
    department=Department.objects.all()
    doctor=Doctor.objects.all()
    form=BookingForm()
    context={
        "department": department,
        "doctor": doctor,
        "form": form,
    }
    if request.method=="POST":
        form=BookingForm(request.POST)
        if form.is_valid():
            form.save()
            form=BookingForm()
            return render(request,"confirmation.html",context)
    return render(request, "our doctors.html",context)




def dashboard_doctor(request):
    return render(request,"doctors/dashboard.html")


def appointment_app(request):
    return render(request,"doctors/doctors_app.html")




def doctor_appointments(request, doctor_id):
    doctor = Doctor.objects.get(pk=doctor_id)
    appointments = doctor.appointments
    return render(request, 'doctor_list.html', {'doctor': doctor, 'appointments': appointments})


def feed_back(request):
    if request.method=="POST":
        form = FeedbackForm(request.POST)
        if form.is_valid():
              form.save()
              messages.success(request,"your message has been sent successfully")
              return redirect('feedconf')
        else:
           form = ContactForm()
          
    return render(request,'feedback.html')


def feedconf(request):
    return render(request,'feedconf.html')

def features(request):
    return render(request,'feature.html')