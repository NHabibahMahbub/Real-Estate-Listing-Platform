from django.db import models


# Create your models here.
class Platform(models.Model):
    property_type_choices = [
        ('Residential', 'Residential'),
        ('Commercial', 'Commercial'),
        ('Land', 'Land'),
        ('Industrial', 'Industrial'),
        ('Special Purpose', 'Special Purpose')
    ]

    title = models.CharField(max_length=100)
    property_type = models.CharField(max_length=20, choices=property_type_choices)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    size_sqft = models.PositiveIntegerField()
    year_built = models.PositiveIntegerField()
    location = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    listed_date = models.DateField(auto_now_add=True)

    # image = models.ImageField()

    def __str__(self):
        return self.title
