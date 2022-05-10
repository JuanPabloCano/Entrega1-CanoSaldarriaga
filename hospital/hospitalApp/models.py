from django.db import models

import uuid


# Create your models here.

class Doctor(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    age = models.IntegerField()
    specialty = models.CharField(max_length=255)
    entrance_time = models.TimeField()
    exit_time = models.TimeField()

    def __str__(self):
        return f"{self.id} - {self.name} {self.last_name}"


class Patient(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    age = models.IntegerField()
    medical_history = models.CharField(max_length=500)

    def __str__(self):
        return f"{self.id} - {self.name} {self.last_name}"


class Parent(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    age = models.IntegerField()
    medical_history = models.CharField(max_length=500)
    patient_relantionship = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.id} - {self.name} {self.last_name}"
