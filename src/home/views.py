from django.shortcuts import render

# Create your views here.
from .forms import BookingForm

def home(request):
		form = BookingForm()
		context = {"form": form}
		template = "home.html"
		return render(request, template, context)