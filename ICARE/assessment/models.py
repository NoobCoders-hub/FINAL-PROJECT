from django.db import models
from django.http import request


class Assessment(models.Model):
    User_Name = models.CharField(max_length=50, null=True, blank=True)
    Body_Temperature = models.CharField(max_length=50, null=True, blank=True)
    Symptom1 = models.CharField(max_length=50, null=True, blank=True)
    Symptom2 = models.CharField(max_length=50, null=True, blank=True)
    Symptom3 = models.CharField(max_length=50, null=True, blank=True)
    Symptom4 = models.CharField(max_length=50, null=True, blank=True)
    Symptom5 = models.CharField(max_length=50, null=True, blank=True)
    Symptom6 = models.CharField(max_length=50, null=True, blank=True)
    Symptom7 = models.CharField(max_length=50, null=True, blank=True)
    Symptom8 = models.CharField(max_length=50, null=True, blank=True)
    Symptom9 = models.CharField(max_length=50, null=True, blank=True)
    Medical_History1 = models.CharField(max_length=50, null=True, blank=True)
    Medical_History2 = models.CharField(max_length=50, null=True, blank=True)
    Medical_History3 = models.CharField(max_length=50, null=True, blank=True)
    Medical_History4 = models.CharField(max_length=50, null=True, blank=True)
    Medical_History5 = models.CharField(max_length=50, null=True, blank=True)
    Medical_History6 = models.CharField(max_length=50, null=True, blank=True)
    Other_Medical_History = models.TextField()
    Vaccinated = models.CharField(max_length=50, null=True, blank=True)
    Vaccine_Name = models.CharField(max_length=50, null=True, blank=True)
    Additional_Info = models.TextField()

    def __str__(self):
        return self.User_Name
