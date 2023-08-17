from django.db import models
import geocoder
# Create your models here.
class Data(models.Model):
    country=models.CharField(max_length=100,null=True)
    population=models.PositiveIntegerField(null=True)
    latitude=models.FloatField(default=0)
    longitude=models.FloatField(default=0)
    
   

    def save(self,*args,**kwargs):
        self.latitude=geocoder.osm(self.country).lat
        self.longitude=geocoder.osm(self.country).lng
        return super().save(*args,**kwargs)

        
    def __str__(self) -> str:
        return self.country
    
    class Enquiry(models.Model):
     name = models.CharField(max_length=50)
     email = models.CharField(max_length=30)
    
    #  message = models.TextField()
    # contact_Message = models.TextField()