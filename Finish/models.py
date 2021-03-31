from django.db import models

# Create your models here.
class Cliente(models.Model):

    id = models.AutoField(primary_key=True)
    Nombre_cliente = models.CharField(max_length=50)
    Dirección_electronico = models.EmailField(max_length=40)
    contra= models.CharField(max_length=60)
    Telefono= models.CharField(max_length=60)
    
    
    
    def __str__(self):
        return self.Nombre_cliente

class Pedido(models.Model):

    id = models.AutoField(primary_key=True)
    Residencia = models.CharField(default='', max_length=100) 
    Telefono= models.CharField(max_length=60)
    Nombre_producto= models.CharField(max_length=60)
    Precio=models.CharField(max_length=60)
    

    
    def __str__(self):
        return self.Residencia



# Create your tests here.