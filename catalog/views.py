from typing import Any
from django.shortcuts import render
from .models import pproducts, categories
from django.views.generic import ListView
from django.contrib.auth.models import User

# Каталог
def main(request):
    context = {
        'title': 'Main',
        'request': request,
    }

    return render(request, 'main.html', context)


# Гитары
class guitars_ListView(ListView):
    model = categories
    context_object_name =  'categories'
    template_name = 'Guitars.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Guitars'
        context['title1'] = 'Гитары'
        return context


# Акустические гитары
def ac_gt(request):
    products = pproducts.objects.all()

    context = {
        'title': 'Acoustic Guitars',
        'products': products,
    }

    return render(request, 'ac_gt.html', context)


# Бас гитары
class bass_gt_ListView(ListView):
    model = pproducts
    template_name = 'bass_gt.html'
    context_object_name = 'products'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Bass Guitars'
        return context

# def bass_gt(request):
#     products = pproducts.objects.all()

#     context = {
#     'title': 'Bass Guitars',
#     'products': products 
#     }

#     return render(request, 'bass_gt.html', context)


# Электро гитары
def electro_gt(request):
    products = pproducts.objects.all()

    context = {
        'title': 'Electro Guitars',
        'products': products,
    }

    return render(request, 'electro_gt.html', context)


# Аксессуары
def dops(request):
    categorys = categories.objects.all()

    context = {
        'title': 'Accessories',
        'title1': 'Аксессуары',
        'categories': categorys
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


class others_ListView(ListView):
    model = pproducts
    context_object_name = 'products'
    template_name = 'dops/others.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Others'
        return context
    

# def others(request):
#     products = pproducts.objects.all()

#     context = {
#         'title': 'Others',
#         'products': products
#     }

#     return render(request, 'dops/others.html', context)

# Доп информация о товаре
def extra_inf(request, pk):
    product = pproducts.objects.filter(pk=pk)
    
    context = {
        'name': product.values('name')[0]['name'],
        'price': product.values('price')[0]['price'],
        'quantity': product.values('quantity')[0]['quantity'],
        'description': product.values('description')[0]['description'],
        'title1': 'Описание',
        'title2': 'Наличие',
        'title3': 'Цена',
        'no_product': 'Нет в наличии',
    }

    return render(request, 'extra_inf.html', context)