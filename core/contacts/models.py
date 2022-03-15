from django.db import models
from django.conf import settings


class Contacts(models.Model):
    """Contacts model"""
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    name = models.CharField(max_length=255, null=False, blank=False)
    email = models.EmailField(max_length=255, null=False, blank=False)
    date_of_birth = models.DateField(null=False, blank=False)
    phone = models.CharField(max_length=20, null=False, blank=False)
    address = models.CharField(max_length=255, null=False, blank=False)
    credit_card = models.CharField(max_length=20, null=False, blank=False)
    franchise = models.CharField(max_length=20, null=False, blank=False)

    def __str__(self):
        return f"{self.id} - {self.name} - {self.email}"
