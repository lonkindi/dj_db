from django.shortcuts import render
from django.urls import reverse

from load_goods.models import Phone


def show_catalog(request):
    sort_me = request.GET.get('sort')
    if sort_me:
        if sort_me == 'min_price':
            sort_me = 'price'
        elif sort_me == 'max_price':
            sort_me = '-price'
    else:
        sort_me = '?'
    phones = Phone.objects.all().order_by(sort_me)
    template = 'load_goods/catalog.html'
    context = {'phones': phones,
               }
    return render(request, template, context)


def show_product(request, slug):
    phone = Phone.objects.filter(slug=slug)
    template = 'load_goods/product.html'
    context = {'phone': phone[0]}
    return render(request, template, context)
