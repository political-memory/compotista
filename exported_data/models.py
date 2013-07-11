from django.db import models


class ExportedRevision(models.Model):
    data = models.TextField()
    checksum = models.CharField(max_length=255)
    creation_datetime = models.DateTimeField()
    last_check_datetime = models.DateTimeField()
