from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Person, Product, Sale
from .forms import PersonForm, ProductForm, SaleForm

# Create your views here.
# Person CRUD
@login_required
def person_list(request):
    search_first_name = request.GET.get('search_first_name', None)
    search_last_name = request.GET.get('search_last_name', None)
    people = Person.objects.all()
    if search_first_name and search_last_name:
        people = people.filter(
            first_name__iexact=search_first_name,
            last_name__iexact=search_last_name
        )
    elif search_last_name or search_first_name:
        people = people.filter(first_name__iexact=search_first_name) \
                 | people.filter(last_name__contains=search_last_name)


    return render(request, 'person_list.html', {'people': people})

@login_required
def person_new(request):
    # ele procura pelo POST, caso o POST esteja vazio o Django cria um form vazio
    form = PersonForm(request.POST or None, request.FILES or None)
    #validar form
    if form.is_valid():
        form.save()
        return redirect('person_list')
    return render(request, 'person_form.html', {'form': form})

@login_required
def person_update(request, id):
    person = get_object_or_404(Person, pk=id) #pk = primary key
    form = PersonForm(request.POST or None, request.FILES or None, instance=person)
    if form.is_valid():
        form.save()
        return redirect('person_list')
    return render(request, 'person_form.html', {'form': form})

@login_required
def person_delete(request, id):
    person = get_object_or_404(Person, pk=id)

    if request.method == 'POST':
        person.delete()
        return redirect('person_list')
    return render(request, 'person_delete_confirm.html', {'person': person})


# Product CRUD
@login_required
def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products' : products})

@login_required
def product_new(request):
    form_product = ProductForm(request.POST or None)
    if form_product.is_valid():
        form_product.save()
        return redirect('product_list')
    return render(request, 'product_form.html', {'form_product' : form_product})

@login_required
def product_update(request, id):
    product = get_object_or_404(Product, pk=id)
    form_product = ProductForm(request.POST or None, instance=product)
    if form_product.is_valid():
        form_product.save()
        return redirect('product_list')
    return render(request, 'product_form.html', {'form_product': form_product})

@login_required
def product_delete(request, id):
    product = get_object_or_404(Product, pk=id)
    if request.method == 'POST':
        product.delete()
        return redirect('product_list')
    return render(request, 'product_delete_confirm.html', {'product': product})

# Safe CRUD
@login_required
def sale_list(request):
    sales = Sale.objects.all()
    return render(request, 'sale_list.html', {'sales': sales})

@login_required
def sale_description(request, id):
    sale = Sale.objects.filter(pk=id).first()
    print('\n\n\n\n')
    print(sale.products.all())
    print('\n\n\n\n')
    products = sale.products.all()
    return render(request, 'sale.html', {'sale' : sale, 'products' : products})

@login_required
def sale_new(request):
    form_sale = SaleForm(request.POST or None)
    if form_sale.is_valid():
        form_sale.save()
        return redirect('sale_list')
    return render(request, 'sale_form.html', {'form_sale' : form_sale})

@login_required
def sale_update(request, id):
    sale = get_object_or_404(Sale, pk=id)
    form_sale = SaleForm(request.POST or None, instance=sale)
    if form_sale.is_valid():
        form_sale.save()
        return redirect('sale_list')
    return render(request, 'sale_form.html', {'form_sale' : form_sale })

@login_required
def sale_delete(request, id):
    sale = get_object_or_404(Sale, pk=id)
    if request.method == 'POST':
        sale.delete()
        return redirect('sale_list')
    return render(request, 'sale_delete_confirm.html', {'sale' : sale})
