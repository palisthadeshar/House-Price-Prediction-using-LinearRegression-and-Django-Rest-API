from django.db import models

# Create your models here.
class price(models.Model):
    MAINROAD_CHOICES=(("Yes","Yes"),("No","No"))
    GUESTROOM_CHOICES=(("Yes","Yes"),("No","No"))
    BASEMENT_CHOICES=(("Yes","Yes"),("No","No"))
    HOTWATER_CHOICES=(("Yes","Yes"),("No","No"))
    AIRCONDITIONING_CHOICES=(("Yes","Yes"),("No","No"))
    PREFAREA_CHOICES=(("Yes","Yes"),("No","No"))
    FURNISHED_CHOICES=(("Semi_furnished","Semi_furnished"),("Unurnished","Unfurnished"))

    area=models.IntegerField(default=0)
    bedrooms=models.IntegerField(default=0)
    bathrooms=models.IntegerField(default=0)
    stories=models.IntegerField(default=0)
    mainroad=models.CharField(max_length=3,choices=MAINROAD_CHOICES)
    guestroom=models.CharField(max_length=3,choices=GUESTROOM_CHOICES)
    basement=models.CharField(max_length=3,choices=BASEMENT_CHOICES)
    hotwaterheating=models.CharField(max_length=3,choices=HOTWATER_CHOICES)
    airconditioning=models.CharField(max_length=3,choices=AIRCONDITIONING_CHOICES)
    parking=models.IntegerField(default=0)
    prefarea=models.CharField(max_length=3,choices=PREFAREA_CHOICES)
    furnished=models.CharField(max_length=15,choices=FURNISHED_CHOICES)
    # unfurnished=models.CharField(max_length=15,choices=FURNISHED_CHOICES)