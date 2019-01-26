from django.forms import ModelForm
from .models import Person, Document, Product, Sale

class PersonForm(ModelForm):

    class Meta:
        model = Person
        fields = ['first_name', 'last_name', 'age', 'salary', 'bio', 'photo']

class DocumentForm(ModelForm):

    class Meta:
        model = Document
        fields = ['num_doc']

class ProductForm(ModelForm):

    class Meta:
        model = Product
        fields = ['description', 'price']

class SaleForm(ModelForm):

    class Meta:
        model = Sale
        fields = ['number', 'value', 'descont', 'tax', 'person', 'products']
