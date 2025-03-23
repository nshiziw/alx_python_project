from django.db import models
from users.models import User

class HouseListing(models.Model):
    STATUS_CHOICES = (
        ('sell', 'For Sale'),
        ('rent', 'For Rent'),
    )
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    bedrooms = models.IntegerField()
    bathrooms = models.IntegerField()
    area = models.DecimalField(max_digits=10, decimal_places=2)
    images = models.JSONField(default=list)  # Store image URLs as a list
    listed_by = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    furnitured = models.BooleanField(default=False)
    nearby_amenities = models.JSONField(default=list)  # Store amenities as a list