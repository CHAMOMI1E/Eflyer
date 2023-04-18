from django.shortcuts import render
from .models import *


def main(request):
    # if request.method == "POST":
    #     user = Users.objects.create(name=request.POST['name'],
    #                                 age=request.POST['age'],
    #                                 adress=request.POST['adress'],
    #                                 id_user=request.POST['id_user']
    #                                 )
    # return render(request, 'crispy.html')
    return render(request, "index.html")


def py_dev(request):
    return render(request, 'python.html')


def sql(request):
    return render(request, 'sql.html')


def flask(request):
    return render(request, 'Flask.html')


def django_dev(request):
    return render(request, 'django.html')
# Create your views here.
