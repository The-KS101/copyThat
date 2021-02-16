from django.db import models

# Create your models here.

class urlTable(models.Model):
    url = models.CharField(max_length=20, blank=False, default = None)
    text = models.TextField(blank=False, default = None)
    deletion_time = models.DateTimeField()

    def __str__(self):
        return self.url