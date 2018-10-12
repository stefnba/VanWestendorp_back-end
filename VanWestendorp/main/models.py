from django.db import models

# Create your models here.

class Answers(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    project = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    exo_toocheap = models.DecimalField(decimal_places=2, max_digits=1000) 
    exo_cheap = models.DecimalField(decimal_places=2, max_digits=1000) 
    exo_epensive = models.DecimalField(decimal_places=2, max_digits=1000) 
    exo_tooexpensive = models.DecimalField(decimal_places=2, max_digits=1000) 
    basis_toocheap = models.DecimalField(decimal_places=2, max_digits=1000) 
    basis_cheap = models.DecimalField(decimal_places=2, max_digits=1000) 
    basis_epensive = models.DecimalField(decimal_places=2, max_digits=1000) 
    basis_tooexpensive = models.DecimalField(decimal_places=2, max_digits=1000) 
    plus_toocheap = models.DecimalField(decimal_places=2, max_digits=1000) 
    plus_cheap = models.DecimalField(decimal_places=2, max_digits=1000) 
    plus_epensive = models.DecimalField(decimal_places=2, max_digits=1000) 
    plus_tooexpensive = models.DecimalField(decimal_places=2, max_digits=1000) 
    dvv_toocheap = models.DecimalField(decimal_places=2, max_digits=1000) 
    dvv_cheap = models.DecimalField(decimal_places=2, max_digits=1000) 
    dvv_epensive = models.DecimalField(decimal_places=2, max_digits=1000) 
    dvv_tooexpensive = models.DecimalField(decimal_places=2, max_digits=1000) 

class Test(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    dvv_epensive = models.DecimalField(decimal_places=2, max_digits=1000) 
