from django.shortcuts import render, redirect
from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    sort = request.GET.get('sort')

    value = Phone.objects.all()

    if sort == 'name':
        value = value.order_by('name')
    elif sort == 'min_price':
        value = value.order_by('price')
    elif sort == 'max_price':
        value = value.order_by('-price')

    template = 'catalog.html'
    context = {'phones': value}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone = Phone.objects.get(slug=slug)
    context = {'phone': phone}
    return render(request, template, context)
