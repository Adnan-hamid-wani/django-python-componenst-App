import DESTINATION
from django.db import models
class Travel(models.Model):
    
    DESTINATION_CHOICES = {('India' , 'India'), ('Paris', 'Paris'),( 'Dubai','Dubai')}
    destinations = models.Charfield(max_length=100, choices = DESTINATION_CHOICES)
    full_name= models.CharField(max_length=100)
    email=models.EmailField()
    check_in_date=models.DateField()
    


# Create your models here
