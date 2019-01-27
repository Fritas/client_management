from django import forms
from .models import Person, Document, Product, Sale

class PersonForm(forms.ModelForm):

    class Meta:
        model = Person
        fields = ['first_name', 'last_name', 'age', 'salary', 'bio', 'photo']

class DocumentForm(forms.ModelForm):

    class Meta:
        model = Document
        fields = ['num_doc']

class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ['description', 'price']

class SaleForm(forms.ModelForm):

    class Meta:
        model = Sale
        fields = ['number', 'value', 'descont', 'tax', 'person', 'products']

