from django.db import models
from django.contrib.auth.models import User


class Users(models.Model):
    name = models.CharField(max_length=30, null=False, blank=False)
    age = models.IntegerField(default=18)
    adress = models.CharField(max_length=30, null=False, blank=False)
    id_user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    basket = models.OneToOneField('Basket', on_delete=models.CASCADE, null=True)


class Category(models.Model):
    name = models.CharField(max_length=30, null=False, blank=False)


class Salesman(models.Model):
    name = models.CharField(max_length=30, null=False, blank=False)
    discription = models.CharField(max_length=30, null=True)


class Raiting(models.Model):
    star = models.IntegerField()


class Comments(models.Model):
    them = models.CharField(max_length=30, null=False, blank=False)
    text = models.CharField(max_length=100, null=True, blank=False)
    user = models.OneToOneField(Users, on_delete=models.CASCADE, null=False)


class Item(models.Model):
    name = models.CharField(max_length=30, null=False, blank=False)
    quantity = models.IntegerField()
    discription = models.CharField(max_length=100, null=True)
    comments = models.ForeignKey(Comments, on_delete=models.CASCADE, null=True)
    category = models.OneToOneField(Category, on_delete=models.CASCADE, null=True)


class Salesmans(models.Model):
    name = models.CharField(max_length=30, null=False, blank=False)
    discription = models.CharField(max_length=100, null=False, blank=False)
    comments = models.ForeignKey(Comments, on_delete=models.CASCADE, null=True)
    items = models.ForeignKey(Item, on_delete=models.CASCADE, null=True)


class Basket(models.Model):
    items = models.ForeignKey(Item, on_delete=models.CASCADE, null=True)
    cost = models.IntegerField()
# Create your models here.
