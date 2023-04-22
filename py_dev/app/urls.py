from django.urls import path
from .views import *

urlpatterns = [
    path('main/', main, name='main'),
    path('py_dev/', py_dev, name='py_dev'),
    path('sql/', sql, name='sql'),
    path('flask/', flask, name='flask'),
    path('django_dev/', django_dev, name='django_dev'),
    path('add_item/', add_item.as_view(), name='add_item'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),

]
