import http

from django.shortcuts import render, redirect
from django.http import HttpResponse
from .admin import Item, Purchase
from django.urls import reverse_lazy
from . import urls
def greetings(request):
    return HttpResponse('Добро пожаловать в наш магазин!')

def list_item(request):
    items = Item.objects.all()
    context = {
        'items': items
    }
    return render(request, 'list_item.html', context)


def detail_item(request, item_id):
    item = Item.objects.get(id=item_id)
    context = {
        'item': item
    }
    return render(request, 'detail_item.html', context)
