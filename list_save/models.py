from django.db import models

# Create your models here.

class Lists(models.Model):
	username = models.CharField(max_length=50)
	email = models.EmailField()
	def __str__(self):
		return self.username
	class Meta:
		db_table = 'Lists'