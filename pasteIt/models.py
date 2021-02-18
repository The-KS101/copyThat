from django.db import models

# Create your models here.


class urlTable(models.Model):
    url = models.CharField(max_length=20, blank=False, primary_key = True)
    text = models.TextField(blank=False, default = None)
    deletion_time = models.DateTimeField()
    visited = models.BooleanField(default=False)       

    def __str__(self):
        return self.url