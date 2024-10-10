from django.db import models

class tododetails(models.Model):
    title = models.CharField(max_length=200)
    details = models.CharField(max_length=300)
    startdate = models.DateField(blank=True, null=True)
    enddate = models.DateField(blank=True, null=True)


   

       

