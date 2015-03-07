from django.shortcuts import render
from django.http import HttpResponseRedirect 
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse

from .forms import BookingForm
from .models import Booking

"""
This will open the home page if the user is already loggedin otherwise it will rediect to the login page.
"""
@login_required
def home(request):
		return render(request, "home/home.html", {})


"""
View for 'click to book' page. If there is no errors in the form then it will be saved and a thanks page will be displayed.
"""
@login_required
def book(request):
	form = BookingForm(request.POST or None)

	if form.is_valid():
		save_it = form.save(commit=False)
		save_it.save()
		return render(request, "home/thanks.html", {})
	context = {"form": form}
	return render(request, "home/book.html", context)

""" 
This view is linked with the "View bookings" page and it will return only those bookings whose status is true 
set(finalized) by the admin.
"""
@login_required
def view(request):
		boo = Booking.objects.filter(status =1)
		return render(request, "home/view.html", {'booking': boo})


"""
This view will list the booking made by loggedin user such that the user can send a cancellation request to admin for the event selected by user.
"""
@login_required
def cancel(request):
		can = Booking.objects.filter(status = 1)
		return render(request, "home/cancel.html", {'cancel': can})


"""
The Logout button calls this view and it will return back to the default login page.
"""
def logout_view(request):
		from django.contrib.auth.views import logout
 		logout(request)
		return HttpResponseRedirect(reverse("home.views.home"))
		# return render(request, "registration/logout.html")
