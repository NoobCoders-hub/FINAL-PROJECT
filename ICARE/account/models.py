from typing import Tuple
from django.db import models
from django.contrib.auth.models import AbstractUser

gender_choices = [
    ["Female", "Female"],
    ["Male", "Male"],
    ["Other", "Other"]
]


class User(AbstractUser):
    is_patient = models.BooleanField('Is patient', default=False)
    is_doctor = models.BooleanField('Is doctor', default=False)
    age = models.CharField(max_length=50,default=1)
    gender = models.CharField(max_length=10, choices=gender_choices, default='none')
