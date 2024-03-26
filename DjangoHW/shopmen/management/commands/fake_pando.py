from django.core.management.base import BaseCommand
from shopmen.models import Product, Order, Client

class Command(BaseCommand):
    help = 'Create base'

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='Client ID')

    def handle(self, *args, **kwargs):
        count = kwargs.get('count')
        client = Client(name='kail', email='312312@mail.ru', phone='123123', address='1231231')
        client.save()
        self.stdout.write(f'{client}')
        for i in range(1, count+1):
            product = Product(name=f'name{i}',
                              description=f'desk{i}',
                              price=1.0+float(i),
                              cnt = 1 * int(i))
            product.save()
            for j in range(1, count + 1):
                order = Order(customer=client,
                              summa=1.0+float(j))
                order.save()
                order.products.add(product)
                self.stdout.write(f'{order}')

