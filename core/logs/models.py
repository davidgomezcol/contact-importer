from django.db import models
from django.conf import settings

STATUS_CHOICES = (
    ('On Hold', 'On Hold'),
    ('Processing', 'Processing'),
    ('Failed', 'Failed'),
    ('Finished', 'Finished'),
)


class FilesStatus(models.Model):
    """File status entries Model"""
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    file_name = models.CharField(max_length=255, blank=False, null=False)
    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default='On Hold'
    )

    def __str__(self):
        return f"{self.file_name} - {self.status}"
