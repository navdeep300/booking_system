from django.contrib import admin
from .models import Booking, Hall

# Register your models here.

class BookingAdmin(admin.ModelAdmin):
	class Meta:
		model = Booking

admin.site.register(Booking, BookingAdmin)

class HallAdmin(admin.ModelAdmin):
	class Meta:
		model = Hall

admin.site.register(Hall, HallAdmin)
