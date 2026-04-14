from django.db import models
from django.contrib.auth.models import User

#classe Mãe:
class Base(models.Model):
    created_at = models.DateTimeField("Creation", auto_now_add=True)
    updated_at = models.DateTimeField("Update", auto_now=True)
    is_deleted = models.BooleanField("Deleted", default=False) #o soft delete para o abstado apagar sem querer

    class Meta:
        abstract = True #para fazer o Djago não criar uma tabela dele

class employee(Base):
    name = models.CharField("Name", max_length=100)

    def __str__(self):
        return self.name
    
class Product(Base):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

class Order(Base):
    client_name = models.CharField(max_length=100)
    products = models.ManyToManyField(Product, related_name='orders')
    
    def __str__(self):
        return f"Order {self.id} - {self.client_name}"

class Profile(Base):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cpf = models.CharField(max_length=14, unique=True)
    photo = models.ImageField(upload_to='profiles/', null=True, blank=True)
    bio = models.TextField(blank=True)

    def __str__(self):
        return f"Profile of {self.user.username}"