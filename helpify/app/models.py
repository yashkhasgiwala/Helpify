from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
from cuser.models import AbstractCUser

class HUser(AbstractCUser):
 	phone = PhoneNumberField()