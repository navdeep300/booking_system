from django.shortcuts import render, HttpResponseRedirect
from django.contrib import auth 

# Create your views here.
def home(request):
		return render(request, "home.html", {})

def book(request):
		return render(request, "book.html", {})

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

