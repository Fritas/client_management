from django.db import models

# Create your models here.
class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=100)
    age = models.PositiveSmallIntegerField()
    salary = models.DecimalField(max_digits=7, decimal_places=2)
    bio = models.TextField()
    photo = models.ImageField(upload_to='person_photos', null=True, blank=True)

    def __str__(self):
        return "%d - %s %s" %(self.id, self.first_name, self.last_name)