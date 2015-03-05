from django import forms
from .models import Booking
from django.contrib.admin import widgets  

class BookingForm(forms.ModelForm):
	date = forms.DateField(widget=widgets.AdminDateWidget)

	class Meta:
		model = Booking 
		fields = ["hall", "date", "start_time", "end_time", "event_name", "name", "email"]
