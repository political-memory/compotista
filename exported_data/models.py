from django.db import models


class ExportRevision(models.Model):
    data = models.TextField()
    checksum = models.CharField(max_length=255)
    datetime = models.DateTimeField()
