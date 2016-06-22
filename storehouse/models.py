from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Provider(models.Model):
    name = models.CharField(max_length=1000, primary_key= True)
    url = models.URLField(blank=True)
    phone = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return self.name


class Ware(models.Model):

    id = models.AutoField(primary_key=True)
    idx = models.IntegerField()
    name = models.CharField(max_length=1000)
    created_date = models.DateTimeField(default=timezone.now)
    created_user = models.ForeignKey('auth.User')
    quantity = models.IntegerField()                            #rozdzielic to na stan magazynowy i na zapotrzebowanie wynikajace ze zlecen
    provider_name = models.CharField(max_length=1000)
    provider_url = models.URLField(blank=True)
    provider = models.ForeignKey(Provider)

    def __str__(self):
        return self.name


class Product(models.Model):

    name = models.CharField(max_length=1000)
    model = models.CharField(max_length=50)
    wareparts = models.ManyToManyField(Ware, blank=True)
    productparts = models.ManyToManyField("self", blank=True)

    def __str__(self):
        return self.name


class Order(models.Model):

    name = models.CharField(max_length=50)
    product = models.ForeignKey(Product)
    status_open = models.BooleanField(default=True)
    client = models.CharField(max_length=50)
    notes = models.CharField(max_length=1000)
    #TODO zwracanie zapotrzebowania

    def __str__(self):
        return self.name


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)

    def __str__(self):
        return self.user.username

