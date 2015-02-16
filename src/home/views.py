from django.shortcuts import render, HttpResponseRedirect,render_to_response
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def home(request):
		return render(request, "home.html")

def book(request):
		return render(request, "book.html")

def view(request):
		return render(request, "view.html")

def cancel(request):
		return render(request, "cancel.html")


# def login(request):
# 	username = request.POST['username']
# 	password = request.POST['password']
# 	user = authenticate(username=username, password=password)
	
# 	if user is not None and user.is_active:
# 		login(request, user)
# 		return HttpResponseRedirect("home.html")
# 	else:
# 		return HttpResponseRedirect("invalid_login.html")


# def logout(request):
# 		logout(request)
#		return render(request,'logout.html')
