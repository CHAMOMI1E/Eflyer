from .models import *


def create_tables():
    user = Users.objects.create(name=request.POST['name'],
                                age=request.POST['age'],
                                adress=request.POST['adress'],
                                id_user=request.POST['id_user']
                                )
