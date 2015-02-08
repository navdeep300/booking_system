from django.contrib import admin
from .models import Booking, Hall

# Register your models here.

class BookingAdmin(admin.ModelAdmin):
	list_display = ['hall', 'event_name', 'name', 'date', 'start_time', 'end_time', 'email', 'status' ]
	class Meta:
		model = Booking

admin.site.register(Booking, BookingAdmin)

class HallAdmin(admin.ModelAdmin):
	list_display = ['hall', 'seats']
	class Meta:
		model = Hall

admin.site.register(Hall, HallAdmin)
