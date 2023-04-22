from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .models import *


def main(request):
    if request.method == "POST":
        user = Users.objects.create(name=request.POST['name'],
                                    age=request.POST['age'],
                                    adress=request.POST['adress'],
                                    id_user=request.POST['id_user']
                                    )
    return render(request, 'index.html')


class add_item(CreateView):
    template_name = "crispy.html"
    model = Item
    fields = ['name', 'quantity', 'discription', 'category']
    success_url = reverse_lazy("add_item")
    context_object_name = "add_item"


def py_dev(request):
    return render(request, 'python.html')


def sql(request):
    return render(request, 'sql.html')


def flask(request):
    return render(request, 'Flask.html')


def django_dev(request):
    return render(request, 'django.html')


class RegisterUser(CreateView):
    form_class = UserCreationForm
    template_name = "crispy.html"
    success_url = reverse_lazy("login")

    def form_valid(self, form):
        user = form.save()
        user.is_staff = True

        user.save()
        login(self.request, user)
        return redirect('main')


class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = "crispy.html"

    def get_success_url(self):
        return reverse_lazy("main")


def logout_user(request):
    logout(request)
    return redirect('main')
