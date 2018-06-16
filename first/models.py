from django.db import models

class Mobile(models.Model):
	manufacturer = models.TextField(blank = True, max_length = 60)
	model_name = models.TextField(blank = True, max_length = 100)

	#Specifications
	display_size = models.FloatField()
	cpu = models.TextField(blank = True, max_length = 100)
	ram = models.DecimalField(max_digits = 3, decimal_places = 0)
	gpu = models.TextField(blank = True, max_length = 100)

	def __str__(self):
		return 'Mobile: {}'.format(self.model_name)
