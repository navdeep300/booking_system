from django import forms
# from django.forms import ModelForm
# from .models import *
# from django.contrib.admin.widgets import AdminDateWidget 
from .models import Booking

class BookingForm(forms.ModelForm):
	class Meta:
		model = Booking 
		fields = ["hall", "date", "start_time", "end_time", "event_name", "name", "email"]

	# hall = forms.CharField()
	# hall = forms.CharField()
	# email = forms.EmailField()
	# date = forms.DateField()

	# date = forms.DateField(widget = AdminDateWidget)

# class select(forms.Form):
#     hall = forms.ModelChoiceField(queryset=hall.objects.all().order_by('name'))
