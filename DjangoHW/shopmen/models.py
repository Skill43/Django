from django.db import models

class Client(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=20)
    registration = models.DateField(auto_now=True)

    def __str__(self):
        return f'Client: {self.name} {self.pk}, email: {self.email}, phone: {self.phone}, address {self.address}'

class Product(models.Model):
    name = models.CharField(max_length=40)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    cnt = models.IntegerField()
    dataapp = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'name: {self.name}, description: {self.description}, price: {self.price}, count {self.cnt}'

class Order(models.Model):
    customer = models.ForeignKey(Client, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    summa = models.DecimalField(max_digits=8, decimal_places=2)
    dataapp = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'Customer: {self.customer.name}, summa: {self.summa}, dataapp: {self.dataapp}'

