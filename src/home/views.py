from django.shortcuts import render
from django.http import HttpResponseRedirect 
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse

from .forms import BookingForm
from .models import Booking

# Create your views here.
@login_required
def home(request):
		return render(request, "home/home.html", {})

@login_required
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
	return render(request, "home/book.html", context)


@login_required
def view(request):
		return render(request, "home/view.html", {})

@login_required
def cancel(request):
		return render(request, "home/cancel.html", {})


def logout_view(request):
		from django.contrib.auth.views import logout
 		logout(request)
		# return HttpResponseRedirect(reverse("home.views.home"))
		return render(request, "registration/logout.html")
