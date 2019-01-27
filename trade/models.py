from django.db import models

# Create your models here.
class Document(models.Model):
    num_doc = models.CharField(max_length=50)


    def __str__(self):
        return "%d - %s" %(self.id, self.num_doc)


class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=100)
    age = models.PositiveSmallIntegerField()
    salary = models.DecimalField(max_digits=7, decimal_places=2)
    bio = models.TextField()
    photo = models.ImageField(upload_to='person_photos', null=True, blank=True)
    doc = models.OneToOneField(Document, null=True, blank=True, on_delete=models.CASCADE)


    def __str__(self):
        return "%d - %s %s" %(self.id, self.first_name, self.last_name)


class Product(models.Model):
    description = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)


    def __str__(self):
        return "%d - %s, $ %.2f" %(self.id, self.description, self.price)


class Sale(models.Model):
    number = models.CharField(max_length=7)
    value = models.DecimalField(max_digits=10, decimal_places=2)
    descont = models.DecimalField(max_digits=5, decimal_places=2)
    tax = models.DecimalField(max_digits=5, decimal_places=2)
    person = models.ForeignKey(Person, null=True, blank=True, on_delete=models.PROTECT)
    products = models.ManyToManyField(Product, blank=True)

    def __str__(self):
        return "%d - %s" %(self.id, self.number)

