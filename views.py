from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from .forms import PersonForm, PersonFormset, user
from django.forms import modelformset_factory
from .models import Person
from django.http import HttpResponse
def register(request):
    form = PersonForm(request.POST)
    if request.method == 'POST':
        form = PersonForm(request.POST)
        print("Hello")
        if form.is_valid():
            form.save()
        else:
            print("notValid")
    return render(request,"home.html", {'form': form})


def personset(request):
    context = {}

    # creating a formset
    GeeksFormSet = modelformset_factory(PersonFormset, fields=['user_name', 'password'], extra = 2)
    formset = GeeksFormSet(request.POST or None)

    # Add the formset to context dictionary
    context['formset'] = formset
    return render(request, "home.html", context)


def list_view(request):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # add the dictionary during initialization
    context["dataset"] = Person.objects.all()

    return render(request, "home.html", context)

def read_view(request, user):
    context = {}
    form = user(request.POST)
    if request.method == 'POST':
        form = user(request.POST)
        print("Hello")
        user_name = form
        try:
            if form.is_valid():
                user_name = form.cleaned_data['user_name']
                user_name = user
                context['dataset'] = Person.objects.get(user_name=user_name)
                print(context['dataset'])
                return render(request, "read.html", context)
        except:
            print("notValid")
            return render(request, "read.html", {'user': user_name})
    return render(request, "read.html", {'form': form})


def update_view(request):
    context = {}
    form = PersonForm(request.POST)
    if request.method == 'POST':
        print("ind")
        if form.is_valid():
            print("Hello")
            user_name = form.cleaned_data['user_name']
            obj = get_object_or_404(Person, user_name = user_name)
            form = PersonForm(request.POST or None, instance=obj)
            form.save()
            context["form"] = form
            return render(request, "update_view.html", context)

    context["form"] = form
    return render(request, "update_view.html", context)


def delete(request):
    context = {}
    form = PersonForm(request.POST)
    if request.method == 'POST':
        print("ind")
        if form.is_valid():
            print("Hello")
            user_name = form.cleaned_data['user_name']
            obj = get_object_or_404(Person, user_name = user_name)
            obj.delete()
            context["form"] = form
            return render(request, "update_view.html", context)

    context["form"] = form
    return render(request, "update_view.html", context)
def hello_geek(request):
    print(request.POST)
    return HttpResponse("HEllogeek")