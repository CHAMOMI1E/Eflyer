from django.urls import path
from .views import *

urlpatterns = [
    path('main/', main, name='main'),
    path('user/', user, name='user'),
    path('sts/', sts, name='sts'),
    path('add_item/', add_item.as_view(), name='add_item'),
    path('RegisterSalesman/', RegisterSalesman.as_view(), name='RegisterSalesman'),
    path('for_salesman/', for_salesman, name='for_salesman'),
    path('show_item/<int:item_id>/', show_item, name="show_item"),
    path('show_comments/', show_comments, name='show_comments'),
    path('search/', Search.as_view(), name='search'),
    path('all_items/', All_items.as_view(), name='all_items'),
    path('login_salesman/', LoginSalesman.as_view(), name='login_salesman'),
    path('salesman/', salesman, name='salesman'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
]
