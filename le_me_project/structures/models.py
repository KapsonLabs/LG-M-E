from django.db import models
from .choices import REGIONS
from accounts.models import User

class District(models.Model):
    created_by              = models.ForeignKey(User, on_delete=models.CASCADE, related_name="district_creator")
    district_name           = models.CharField(max_length=100)
    district_region         = models.CharField(max_length=20, choices=REGIONS)
    district_size_hectares  = models.IntegerField()
    date_created            = models.DateTimeField(auto_now_add=True)

class DistrictStaff(models.Model):
    district_related        = models.ForeignKey(District, on_delete=models.CASCADE, related_name="related_district_staff")
    user_related            = models.ForeignKey(User, on_delete=models.CASCADE, related_name="district_staff")
    staff_role              = models.CharField(max_length=25)
    staff_contact           = models.CharField(max_length=25)
    active                  = models.BooleanField(default=False)
    date_created            = models.DateTimeField(auto_now_add=True)

class Subcounty(models.Model):
    created_by                  = models.ForeignKey(User, on_delete=models.CASCADE, related_name="subcounty_creator")
    district_related            = models.ForeignKey(District, on_delete=models.CASCADE, related_name="related_district_subcounty")
    subcounty_name              = models.CharField(max_length=100)
    subcounty_size_hectares     = models.IntegerField()
    date_created                = models.DateTimeField(auto_now_add=True)

class SubcountyStaff(models.Model):
    district_related        = models.ForeignKey(District, on_delete=models.CASCADE, related_name="related_subcounty_staff")
    user_related            = models.ForeignKey(User, on_delete=models.CASCADE, related_name="subcounty_staff")
    staff_role              = models.CharField(max_length=25)
    staff_contact           = models.CharField(max_length=25)
    active                  = models.BooleanField(default=False)
    date_created            = models.DateTimeField(auto_now_add=True)

class Parish(models.Model):
    created_by                  = models.ForeignKey(User, on_delete=models.CASCADE, related_name="parish_creator")
    subcounty_related           = models.ForeignKey(Subcounty, on_delete=models.CASCADE, related_name="related_subcounty_parish")
    parish_name                 = models.CharField(max_length=100)
    parish_size_hectares        = models.IntegerField()
    date_created                = models.DateTimeField(auto_now_add=True)

class ParishStaff(models.Model):
    parish_related          = models.ForeignKey(Parish, on_delete=models.CASCADE, related_name="related_parish_staff")
    user_related            = models.ForeignKey(User, on_delete=models.CASCADE, related_name="parish_staff")
    staff_role              = models.CharField(max_length=25)
    staff_contact           = models.CharField(max_length=25)
    active                  = models.BooleanField(default=False)
    date_created            = models.DateTimeField(auto_now_add=True)

class Cell(models.Model):
    created_by                  = models.ForeignKey(User, on_delete=models.CASCADE, related_name="cell_creator")
    parish_related              = models.ForeignKey(Parish, on_delete=models.CASCADE, related_name="related_parish_cell")
    cell_name                   = models.CharField(max_length=100)
    cell_size_hectares          = models.IntegerField()
    date_created                = models.DateTimeField(auto_now_add=True)

class CellStaff(models.Model):
    district_related        = models.ForeignKey(Cell, on_delete=models.CASCADE, related_name="related_cell_staff")
    user_related            = models.ForeignKey(User, on_delete=models.CASCADE, related_name="cell_staff")
    staff_role              = models.CharField(max_length=25)
    staff_contact           = models.CharField(max_length=25)
    active                  = models.BooleanField(default=False)
    date_created            = models.DateTimeField(auto_now_add=True)
