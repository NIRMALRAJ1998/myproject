from django.db import models

from .careermodels import CareerApplication


class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    

    def __str__(self):
        return self.subjectz