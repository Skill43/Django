from django.core.management.base import BaseCommand
from shopmen.models import Client

class Command(BaseCommand):
    help = 'Create base'

    def handle(self, *args, **options):
        # client = Client(name='Pavel', email='123@mail.ru', phone='123123123', address='mozir')
        # client = Client(name='Cova', email='3213@mail.ru', phone='123123', address='Gomel')
        client.save()
        self.stdout.write(f'{client}')