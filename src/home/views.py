from django.shortcuts import render

# Create your views here.
# from .forms import BookingForm

# def home(request):
# 		form = BookingForm()
# 		context = {"form": form}
# 		template = "home.html"
# 		return render(request, template, context)

def home(request):
		return render(request, "home.html", {})

def book(request):
		return render(request, "book.html", {})

def view(request):
		return render(request, "view.html", {})

def cancel(request):
		return render(request, "cancel.html", {})
