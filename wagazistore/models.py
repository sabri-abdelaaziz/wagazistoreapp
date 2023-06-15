from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='product_images/')





class Contact(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return self.name

class Person(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    telephone = models.CharField(max_length=20)

    class Meta:
        db_table = 'person'


from django.db import models

class Satisfaction(models.Model):
    id_user = models.IntegerField()
    stars = models.IntegerField()


