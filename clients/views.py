from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Person
from .forms import PersonForm

# Create your views here.
@login_required
def person_list(request):
    people = Person.objects.all()
    return render(request, 'person_list.html', {'people': people})


@login_required
def person_new(request):
    # ele procura pelo POST, caso o POST esteja vazio o Django cria um form vazio
    form = PersonForm(request.POST or None, request.FILES or None)
    #validar form
    if form.is_valid():
        form.save()
        return redirect('person_list')
    return render(request, 'personform.html', {'form': form})


@login_required
def person_update(request, id):
    person = get_object_or_404(Person, pk=id) #pk = primary key
    form = PersonForm(request.POST or None, request.FILES or None, instance=person)
    if form.is_valid():
        form.save()
        return redirect('person_list')
    return render(request, 'personform.html', {'form': form})


@login_required
def person_delete(request, id):
    person = get_object_or_404(Person, pk=id)
    form = PersonForm(request.POST or None, request.FILES or None, instance=person)

    if request.method == 'POST':
        person.delete()
        return redirect('person_list')
    return render(request, 'person_delete_confirm.html', {'person': person})