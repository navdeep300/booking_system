from django.db import models

# Create your models here.

class Booking(models.Model):
	date = models.DateField(auto_now = False, auto_now_add = False)
	start_time = models.TimeField(auto_now=False, auto_now_add=False)
	end_time = models.TimeField(auto_now=False, auto_now_add=False)
	email = models.EmailField('Email', max_length=50)
	event_name = models.CharField(max_length=50)
	name = models.CharField(max_length=50)
	status = models.BooleanField(default=False)
	hall = models.ForeignKey('Hall')
	
	class Meta:
    		unique_together = ('hall', 'start_time', 'end_time',)
	
	def __unicode__(self):
		return self.event_name	

class Hall(models.Model):
	hall = models.CharField(max_length=25, unique=True)
	seats = models.PositiveSmallIntegerField()
	
	def __unicode__(self):
		return self.hall
	
