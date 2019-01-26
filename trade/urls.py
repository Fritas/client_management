from django.urls import path
from .views import person_list, person_new, person_update, person_delete
from .views import product_list, product_new, product_update, product_delete
from .views import sale_description, sale_list, sale_new, sale_update, sale_delete

urlpatterns = [
    #client
    path('client/list', person_list, name="person_list"),
    path('client/new', person_new, name="person_new"),
    path('client/update/<int:id>', person_update, name="person_update"),
    path('client/delete/<int:id>', person_delete, name="person_delete"),
    #product
    path('product/list', product_list, name="product_list"),
    path('product/new', product_new, name="product_new"),
    path('product/update/<int:id>', product_update, name="product_update"),
    path('product/delete/<int:id>', product_delete, name="product_delete"),
    #sale
    path('sale/description/<int:id>', sale_description, name="sale"),
    path('sale/list', sale_list, name="sale_list"),
    path('sale/new', sale_new, name="sale_new"),
    path('sale/update/<int:id>', sale_update, name="sale_update"),
    path('sale/delete/<int:id>', sale_delete, name="sale_delete"),
]