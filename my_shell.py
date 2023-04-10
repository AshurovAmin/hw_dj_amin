import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'web_project.settings')
django_asgi_app = get_asgi_application()

from shop.models import Item, Purchase

item = Item.objects.create(name='bmw', price='150000')
shop1 = Item.objects.create(name='audi', price='150000')
shop2 = Item.objects.create(name='mers', price='50000')
shop3 = Item.objects.create(name='posche', price='150000')
shop4 = Item.objects.create(name='Urus', price='250000')
shop5 = Item.objects.create(name='RR', price='2250000')
shop6 = Item.objects.create(name='Honqhi', price='150000')
shop7 = Item.objects.create(name='Land Rover', price='250000')
shop8 = Item.objects.create(name='Golf', price='5000')
shop9 = Item.objects.create(name='Brabus', price='250000')
shop10 = Item.objects.create(name='M5F90', price='200000')

Purchase.objects.create(name='Car', age='20', item=item)
Purchase.objects.create(name='Car', age='20', item=item)
Purchase.objects.create(name='Car', age='20', item=item)
Purchase.objects.create(name='Car', age='20', item=item)
Purchase.objects.create(name='Car', age='20', item=item)
Purchase.objects.create(name='Car', age='20', item=item)
Purchase.objects.create(name='Car', age='20', item=item)
Purchase.objects.create(name='Car', age='20', item=item)
Purchase.objects.create(name='Car', age='20', item=item)
Purchase.objects.create(name='Car', age='20', item=item)
Purchase.objects.create(name='Car', age='20', item=item)
Purchase.objects.create(name='Car', age='20', item=item)
Purchase.objects.create(name='Car', age='20', item=item)
Purchase.objects.create(name='Car', age='20', item=item)
Purchase.objects.create(name='Car', age='20', item=item)
Purchase.objects.create(name='Car', age='20', item=item)
Purchase.objects.create(name='Car', age='20', item=item)
Purchase.objects.create(name='Car', age='20', item=item)
Purchase.objects.create(name='Car', age='20', item=item)
Purchase.objects.create(name='Car', age='20', item=item)
