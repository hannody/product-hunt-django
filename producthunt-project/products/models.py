from django.db import models
import datetime
from django.contrib.auth.models import User

class Product(models.Model):

	title		= models.CharField(max_length = 250)

	url     	= models.URLField(max_length = 200, blank = True)

	pub_date    = models.DateTimeField(null = True)

	image 		= models.ImageField(upload_to ='images/')

	icon 		= models.ImageField(upload_to = 'images/')

	body 		= models.TextField(max_length = 500)

	votes_total = models.IntegerField(default = 1)

	hunter 		= models.ForeignKey(User, on_delete=models.CASCADE, blank = True)

	def __str__(self):
		return self.title
	
	def pub_date_pr(self):
		return self.pub_date.strftime('%e %b %Y')

	def summary(self):
		return self.body[:100]