from django.urls import path
from .views import *

urlpatterns = [
    path('main/', main, name='main'),
    path('py_dev/', py_dev, name='py_dev'),
    path('sql/', sql, name='sql'),
    path('flask/', flask, name='flask'),
    path('django_dev/', django_dev, name='django_dev')

]
