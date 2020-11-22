from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import MinLengthValidator, RegexValidator
from django.conf import settings

# Create your models here.
from cuser.models import AbstractCUser

class HUser(AbstractCUser):
	phone = PhoneNumberField()
	reg_plate1 = models.CharField(max_length=10,
		validators=[MinLengthValidator(10, message="Enter valid license plate number"),
		RegexValidator('^[A-Z]{2}[0-9]{2}[A-Z]{2,3}[0-9]{4}$', message="Enter valid license plate number")])
	contact_phone1 = PhoneNumberField()


class Report(models.Model):
	image = models.ImageField(upload_to="uploads/%Y/%m/%d")
	reg_plate = models.CharField(max_length=10,null=False,
		validators=[MinLengthValidator(10, message="Enter valid license plate number"),
		RegexValidator('^[A-Z]{2}[0-9]{2}[A-Z]{2,3}[0-9]{4}$', message="Enter valid license plate number")])
	ip = models.CharField(max_length=20, blank=True)
	latitude = models.DecimalField(max_digits=10, decimal_places=8, null=True)
	longitude = models.DecimalField(max_digits=11, decimal_places=8, null=True)

	def __str__(self):
		"""String for representing the Model object."""
		return self.reg_plate

# class RegisteredPlates(models.Model):
# 	owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE);
# 	reg_plate = models.CharField(max_length=10,null=False,
# 		validators=[MinLengthValidator(10, message="Enter valid license plate number"),
# 		RegexValidator('^[A-Z]{2}[0-9]{2}[A-Z]{2,3}[0-9]{4}$', message="Enter valid license plate number")])
	

# 	def __str__(self):
# 		"""String for representing the Model object."""
# 		return self.reg_plate