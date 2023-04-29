from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, FormView
from .forms import *

from .models import *


def main(request):
    return render(request, 'index.html')


def user(request):
    usernames = request.user.id
    user_info = Users.objects.get(id_user=usernames)
    if request.method == "POST":
        user_info.name = request.POST['name']
        user_info.age = request.POST['age']
        user_info.adress = request.POST['adress']
        user_info.save()
        redirect("/app/main")
    return render(request, "user.html", {"user": user_info})


def sts(request):
    return render(request, 'in.html')


class for_salesman(ListView):
    template_name = "for_salesmans.html"
    model = Item
    context_object_name = "Items"
    paginate_by = 9


def show_item(request, item_id):
    item = Item.objects.get(id=item_id)
    return render(request, 'item.html', {'item': item})


class add_item(FormView):
    template_name = 'crispy.html'
    form_class = ItemForm
    success_url = '/for_salesman'

    def form_valid(self, form):
        new_item = form.save()
        item = Item.objects.get(id=new_item.id)
        user = User.objects.get(username=self.request.user.username)
        sale = Salesmans.objects.get(id_user=user)
        sale.items.add(item)
        return redirect('for_salesman')


class RegisterUserSale(CreateView):
    form_class = UserCreationForm
    template_name = "crispy.html"
    success_url = reverse_lazy("login")

    def form_valid(self, form):
        user = form.save()
        user.is_staff = True

        user.save()

        login(self.request, user)
        new_user = Users(id_user=user)
        new_user.save()
        return redirect('main')
        # return redirect('add_user')


class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = "crispy.html"

    def get_success_url(self):
        return reverse_lazy("main")


class RegisterUser(CreateView):
    form_class = UserCreationForm
    template_name = "crispy.html"
    success_url = reverse_lazy("login")

    def form_valid(self, form):
        user = form.save()
        user.is_staff = True

        user.save()

        login(self.request, user)
        new_basket = Basket.objects.create()
        new_basket.save()
        new_user = Users(id_user=user, basket=new_basket)
        new_user.save()
        return redirect('main')
        # return redirect('add_user')


class RegisterSalesman(CreateView):
    form_class = UserCreationForm
    template_name = "crispy.html"
    success_url = reverse_lazy("login")

    def form_valid(self, form):
        user = form.save()
        user.is_staff = True

        user.save()

        login(self.request, user)
        new_sale = Salesmans(id_user=user)
        new_sale.save()
        return redirect('for_salesman')


class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = "crispy.html"

    def get_success_url(self):
        return reverse_lazy("main")


def logout_user(request):
    logout(request)
    return redirect('main')
