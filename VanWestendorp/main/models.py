from django.db import models

# Create your models here.

def valid_pct(val):
    if val.endswith("%"):
       return float(val[:-1])/100
    else:
       try:
          return float(val)
       except ValueError:          
          raise ValidationError(
              _('%(value)s is not a valid pct'),
                params={'value': value},
           )

class Answers(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    project = models.CharField(max_length=255, blank=True, null=True)
    client_segment = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    exo_toocheap = models.CharField(max_length=255, validators=[valid_pct]) 
    exo_cheap = models.CharField(max_length=255, validators=[valid_pct]) 
    exo_epensive = models.CharField(max_length=255, validators=[valid_pct]) 
    exo_tooexpensive = models.CharField(max_length=255, validators=[valid_pct]) 
    basis_toocheap = models.CharField(max_length=255, validators=[valid_pct]) 
    basis_cheap = models.CharField(max_length=255, validators=[valid_pct]) 
    basis_epensive = models.CharField(max_length=255, validators=[valid_pct]) 
    basis_tooexpensive = models.CharField(max_length=255, validators=[valid_pct]) 
    plus_toocheap = models.CharField(max_length=255, validators=[valid_pct]) 
    plus_cheap = models.CharField(max_length=255, validators=[valid_pct]) 
    plus_epensive = models.CharField(max_length=255, validators=[valid_pct]) 
    plus_tooexpensive = models.CharField(max_length=255, validators=[valid_pct]) 
    dvv_toocheap = models.CharField(max_length=255, validators=[valid_pct]) 
    dvv_cheap = models.CharField(max_length=255, validators=[valid_pct]) 
    dvv_epensive = models.CharField(max_length=255, validators=[valid_pct]) 
    dvv_tooexpensive = models.CharField(max_length=255, validators=[valid_pct]) 
