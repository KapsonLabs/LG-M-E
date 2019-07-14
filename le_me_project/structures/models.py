from django.db import models
from .choices import REGIONS

class District(models.Model):
    district_name           = models.CharField(max_length=100)
    district_region         = models.CharField(max_length=20, choices=REGIONS)
    district_size_hectares  = models.IntegerField()
    date_created            = models.DateTimeField(auto_now_add=True)
