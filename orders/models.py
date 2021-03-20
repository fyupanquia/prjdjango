from django.db import models

# Create your models here.
class Client(models.Model):
    name=models.CharField(max_length=30)
    address = models.CharField(max_length=30,verbose_name='Dirección')
    email=models.EmailField(blank=True, null=True)
    phone=models.CharField(max_length=7)
    
    #def __str__(self):
    #    return self.name
       
class Article(models.Model):
    name=models.CharField(max_length=30)
    section = models.CharField(max_length=20)
    price=models.IntegerField()

    def __str__(self):
        return 'name: %s, section: %s, price: %s' % (self.name, self.section, self.price)

class Order(models.Model):
    number=models.IntegerField()
    date=models.DateField()
    delivered=models.BooleanField()
