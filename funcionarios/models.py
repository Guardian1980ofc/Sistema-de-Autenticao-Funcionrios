from django.db import models

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
    

