from django.shortcuts import render,redirect
from .forms import person_form
from .models import pproducts

#Каталог
def main(request):
    context = {
        'title': 'Main'
    }

    return render(request, 'main.html', context)


#Акустические гитары
def ac_gt(request):

    products = pproducts.objects.all()
    context = {
        'title': 'Acoustic Guitars',
        'products': products,
    }

    return render(request, 'ac_gt.html', context)


#Бас гитары
def bass_gt(request):
    products = pproducts.objects.all()

    context = {
    'title': 'Bass Guitars',
    'products': products 
    }

    return render(request, 'bass_gt.html', context)


#Электро гитары
def electro_gt(request):
    products = pproducts.objects.all()

    context = {
        'title': 'Electro Guitars',
        'products': products,
    }

    return render(request, 'electro_gt.html', context)


#Аудентиф
def auth(request):
    if request.method == 'POST':
        form = person_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Main')
        else:
            error = 'Error'

    form = person_form()
    context = {
        'form': form
    }
    return render(request, 'auth.html', context)



#Аксессуары
def dops(request):
    products = pproducts.objects.all()

    context = {
        'title': 'Accessories',
        'products': products
    }

    return render(request, 'dops.html', context)



def strings(request):
    products = pproducts.objects.all()

    context = {
        'title': 'Strings',
        'products': products
    }

    return render(request, 'dops/strings.html', context)


def mediators(request):
    products = pproducts.objects.all()

    context = {
        'title': 'Mediators',
        'products': products
    }

    return render(request, 'dops/mediators.html', context)


def capo(request):
    products = pproducts.objects.all()

    context = {
        'title': 'Capo',
        'products': products
    }

    return render(request, 'dops/capo.html', context)


def others(request):
    products = pproducts.objects.all()

    context = {
        'title': 'Others',
        'products': products
    }

    return render(request, 'dops/others.html', context)