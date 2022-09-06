from django.db import models

class Discount(models.Model):
    key= models.BigAutoField(primary_key=True)
    website = models.CharField(max_length=300)
    code = models.CharField(max_length=255)
    icon = models.CharField(max_length=255)
    precent = models.IntegerField()

    def __str__(self) :
        return self.code
   
