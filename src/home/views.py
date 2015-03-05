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
		return render(request, "home/thanks.html", {})
	context = {"form": form}
	return render(request, "home/book.html", context)


@login_required
def view(request):
		boo = Booking.objects.filter(status =1)
		return render(request, "home/view.html", {'boo': boo})

@login_required
def cancel(request):
		return render(request, "home/cancel.html", {})


def logout_view(request):
		from django.contrib.auth.views import logout
 		logout(request)
		return HttpResponseRedirect(reverse("home.views.home"))
		# return render(request, "registration/logout.html")