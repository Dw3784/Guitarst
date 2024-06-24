from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from .models import pproducts, categories
from django.views.generic import ListView
from django.contrib.auth.models import User
from django.core.paginator import Paginator


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


# Функция для пагинации
def get_pagination(model, request, category):
    model = model

    products = model.objects.filter(category=category)

    pagination = Paginator(products, 4)# разбиение по страницам
    page_number = request.GET.get('page')# количество страниц
    page = pagination.get_page(page_number)# страница для отображения
    return [page, pagination]


# Акустические гитары
def ac_gt(request):
    pagin = get_pagination(pproducts, request, category='ac-gt')
    
    products = pagin[0]
    paginator = pagin[1]
    for product in products:
        print(product.image.url)
    
    context = {
        'title': 'Acoustic Guitars',
        'title1': 'Акустические гитары',
        'products': products,
        'paginator': paginator,
    }

    return render(request, 'ac_gt.html', context)


# Бас гитары
def bass_gt(request):
    pagin = get_pagination(pproducts, request, category='bass-gt')

    products = pagin[0]
    paginator = pagin[1]

    context = {
        'title': 'Bass Guitars',
        'title1': 'Бас гитары',
        'products': products ,
        'paginator': paginator, 
    }

    return render(request, 'bass_gt.html', context)


# Электро гитары
def electro_gt(request):
    pagin = get_pagination(pproducts, request, category='el-gt')

    products = pagin[0]
    paginator = pagin[1]

    context = {
        'title': 'Electro Guitars',
        'products': products,
        'paginator': paginator,
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


# Струны
def strings(request):
    pagin = get_pagination(pproducts, request, category='strings')

    products = pagin[0]
    paginator = pagin[1]

    context = {
        'title': 'Strings',
        'title1': 'Струны',
        'products': products,
        'paginator': paginator,
    }

    return render(request, 'dops/strings.html', context)


# Медиаторы
def mediators(request):
    pagin = get_pagination(pproducts, request, category='mediators')

    products = pagin[0]
    paginator = pagin[1]

    context = {
        'title': 'Mediators',
        'title1': 'Медиаторы',
        'products': products,
        'paginator': paginator,
    }

    return render(request, 'dops/mediators.html', context)


# Каподастры
def capo(request):
    pagin = get_pagination(pproducts, request, category='capo')

    products = pagin[0]
    paginator = pagin[1]

    context = {
        'title': 'Capo',
        'title1': 'Каподастры',
        'products': products,
        'paginator': paginator,
    }

    return render(request, 'dops/capo.html', context)
    

# Другие товары
def others(request):
    pagin = get_pagination(pproducts, request, category='others')

    products = pagin[0]
    paginator = pagin[1]

    context = {
        'title': 'Others',
        'title1': 'Другое',
        'products': products,
        'paginator': paginator,
    }

    return render(request, 'dops/others.html', context)


# Доп информация о товаре
def extra_inf(request, pk):
    product = pproducts.objects.filter(pk=pk)
    
    context = {
        'name': product.values('name')[0]['name'],
        'price': product.values('price')[0]['price'],
        'quantity': product.values('quantity')[0]['quantity'],
        'description': product.values('description')[0]['description'],
        'product': product,
        'title1': 'Описание',
        'title2': 'Наличие',
        'title3': 'Цена',
        'no_product': 'Нет в наличии',
    }

    return render(request, 'extra_inf.html', context)