from django.db import models
from users.models import User

from django.contrib.auth.models import PermissionsMixin

# Create entity savings
class Savings(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
	days = models.IntegerField()
	numbers = models.IntegerField()
	total_savings = models.IntegerField(default=0)

	created_at = models.DateField(auto_now_add=True)
	updated_at = models.DateField(auto_now_add=True)

	class Meta:
		db_table = 'savings'
		ordering = ["-updated_at"]

	def __str__(self):
		return str(self.user)

