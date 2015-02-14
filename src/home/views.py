from django.shortcuts import render, HttpResponseRedirect
from django.contrib import auth 

# Create your views here.
from .forms import BookingForm
from .models import Booking

# def home(request):
# 		form = BookingForm()
# 		context = {"form": form}
# 		template = "home.html"
# 		return render(request, template, context)
def home(request):
	return render(request, "home.html", {})

def book(request):

	form = BookingForm(request.POST or None)

	if form.is_valid():
		save_it = form.save(commit=False)
		save_it.save()
		# print request.POST["email"], request.POST["email_2"]
		# form = BookingForm(request.POST or None)
		# if form.is_valid():
		# 	email = form.cleaned_data['email']
		# 	hall = form.cleaned_data['hall']
		# 	date = form.cleaned_data['date']
		# 	email_join, created = Booking.objects.get_or_create(email=email)
		# 	hall_entry, created3 = Booking.objects.get_or_create(hall=hall)
		# 	date, created2 = Booking.objects.get_or_create(date=date)	
		# 	print hall_entry, created3, email_join, created, date, created2

	context = {"form": form}
	return render(request, "book.html", context)

def view(request):

	return render(request, "view.html", {})

def cancel(request):
	return render(request, "cancel.html", {})


def login_view(request):
	username = request.POST.get('username', '')
	password = request.POST.get('password', '')
	user = auth.authenticate(username=username, password=password)
	if user is not None and user.is_active:
		auth.login(request, user)
		return HttpResponseRedirect("/account/loggedin/")
	else:
		return HttpResponseRedirect("/account/invalid/")

def logout_view(request):
	auth.logout(request)
	return HttpResponseRedirect("/accounts/loggedout/")

