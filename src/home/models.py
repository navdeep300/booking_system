from django.db import models

# Create your models here.
"""
It contains the informations of the current booking status of various halls it should have unique hall and date and time values.
If the hall is already booked its booking_status will be True, otherwise False
"""
class Booking(models.Model):
	hall = models.ForeignKey('Hall')
	date = models.DateField(auto_now=False, auto_now_add=False)
	start_time = models.TimeField(auto_now=False, auto_now_add=False)
	end_time = models.TimeField(auto_now=False, auto_now_add=False)
	name = models.CharField(max_length=50)
	email = models.EmailField('Email', max_length=50)
	event_name = models.CharField(max_length=50, unique=True)
	status = models.BooleanField(default=False)
	
	
	class Meta:
    		unique_together = ('hall', 'start_time', 'end_time',)
	
	def __unicode__(self):
		return self.event_name	


"""
It contains the information about the Hall, i.e. what is the name of the hall and its other hall featured related informations.
"""
class Hall(models.Model):
	hall = models.CharField(max_length=25, unique=True)
	seats = models.PositiveSmallIntegerField()
	
	def __unicode__(self):
		return self.hall
	
