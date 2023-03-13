from django.db import models
from users.models import User

from django.contrib.auth.models import PermissionsMixin

# Create entity savings
class Days(models.Model):
	n_days = models.IntegerField(unique=True, null=True)

	class Meta:
		db_table = 'days'

	def __str__(self):
		return str(self.n_days)

class Numbers(models.Model):
	numeros = models.IntegerField(unique=True, null=True)

	class Meta:
		db_table = 'numbers'

	def __str__(self):
		return str(self.numeros)

class Savings(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
	days = models.ForeignKey(Days, on_delete=models.CASCADE, null=True)
	numbers = models.ManyToManyField(Numbers)
	

	created_at = models.DateField(auto_now_add=True)
	updated_at = models.DateField(auto_now_add=True)

	class Meta:
		db_table = 'savings'
		ordering = ["-updated_at"]

	def __str__(self):
		return str(self.user)

