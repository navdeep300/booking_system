from django import forms
from .models import Booking
from django.contrib.admin import widgets  

class BookingForm(forms.ModelForm):
	# With the help of the AdminDateWidget, a calender for the date input can be used.
	date = forms.DateField(widget=widgets.AdminDateWidget)

	# This connects the 'Booking' model with this form and shows the specified fields on the html.
	class Meta:
		model = Booking 
		fields = ["hall", "date", "start_time", "end_time", "event_name", "name", "email"]