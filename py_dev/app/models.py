from django.db import models
from django.contrib.auth.models import User


class Users(models.Model):
    name = models.CharField(max_length=30, null=False, blank=False)
    age = models.IntegerField(default=18)
    adress = models.CharField(max_length=30, null=False, blank=False)
    id_user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    basket = models.OneToOneField('Basket', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=30, null=False, blank=False)

    def __str__(self):
        return self.name


class Raiting(models.Model):
    star = models.IntegerField()

    def __str__(self):
        return self.star


class Comments(models.Model):
    them = models.CharField(max_length=30, null=False, blank=False)
    text = models.CharField(max_length=100, null=True, blank=False)
    user = models.OneToOneField(Users, on_delete=models.CASCADE, null=False)

    def __str__(self):
        return self.them


class Item(models.Model):
    name = models.CharField(max_length=30, null=False, blank=False)
    quantity = models.IntegerField(default=1)
    price = models.IntegerField(default=100)
    discription = models.CharField(max_length=100, null=True)
    comments = models.ForeignKey(Comments, on_delete=models.CASCADE, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    photo = models.ImageField(upload_to='items_photo', null=True)

    def __str__(self):
        return self.name


class Salesmans(models.Model):
    name = models.CharField(max_length=30, null=False, blank=False)
    discription = models.CharField(max_length=100, null=False, blank=False)
    comments = models.ForeignKey(Comments, on_delete=models.CASCADE, null=True)
    items = models.ManyToManyField(Item)
    id_user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name


class Basket(models.Model):
    items = models.ManyToManyField(Item)
    cost = models.IntegerField(default=0)

    def __str__(self):
        return str(self.id)
# Create your models here.
