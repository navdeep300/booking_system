from django.shortcuts import render

# Create your views here.
#from .forms import BookingForm

def home(request):
		#form = BookingForm()
		context = {}
		template = "home.html"
		return render(request, template, context)

def book(request):
		#form = BookingForm()
		context = {}
		template = "book.html"
		return render(request, template, context)

def view(request):
		#form = BookingForm()
		context = {}
		template = "view.html"
		return render(request, template, context)

def cancel(request):
		#form = BookingForm()
		context = {}
		template = "cancel.html"
		return render(request, template, context)
