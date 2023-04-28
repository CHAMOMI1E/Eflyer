from django.urls import path
from .views import *

urlpatterns = [
    path('main/', main, name='main'),
    path('user/', user, name='user'),
    path('sts/', sts, name='sts'),
    path('add_item/', add_item.as_view(), name='add_item'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    # path('add_user/', add_user.as_view(), name='add_user'),
    path('for_salesman/', for_salesman, name='for_salesman'),

]
