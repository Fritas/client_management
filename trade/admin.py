from django.contrib import admin
from .models import Person, Document, Sale, Product

# Register your models here.
admin.site.register(Person)
admin.site.register(Document)
admin.site.register(Sale)
admin.site.register(Product)