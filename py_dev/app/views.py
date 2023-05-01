from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from django.http import HttpResponse
from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.models import Permission, Group
from django.views.generic import CreateView, ListView, FormView
from .forms import *

from .models import *


def main(request):
    items = Item.objects.all()
    return render(request, 'search_result.html', {"items": items})



@permission_required('user.change_user', login_url='../../app/login')
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


@permission_required('salesmans.change_salesmans', login_url='../../app/login_salesman')
def salesman(request):
    usernames = request.user.id
    user_info = Salesmans.objects.get(id_user=usernames)
    if request.method == "POST":
        user_info.name = request.POST['name']
        user_info.discription = request.POST['discription']
        user_info.save()
        redirect("/app/main")
    return render(request, "salesman.html", {"user": user_info})


def sts(request):
    return render(request, 'in.html')


@permission_required('item.add_item', login_url='../../app/login_salesman')
def for_salesman(request):
    if request.user.is_authenticated:
        user = User.objects.get(username=request.user.username)
        sale = Salesmans.objects.get(id_user=user)
        items = sale.items.all()
        return render(request, 'for_salesmans.html', {'items': items})
    else:
        return redirect('login_salesman')


#

@permission_required('comments.add_comments', login_url='../../logout')
def show_item(request, item_id):
    item = Item.objects.get(id=item_id)
    return render(request, 'item.html', {'item': item})


def show_comments(requset):
    return render(requset, "comments.html")


# @permission_required('item.add_item', login_url='/login_salesman')
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


class RegisterSalesman(CreateView):
    form_class = UserCreationForm
    template_name = "crispy.html"
    success_url = reverse_lazy("login_salesman")

    def form_valid(self, form):
        user = form.save()
        user.is_staff = True
        group_reg = Group.objects.get(name='salesman')
        user.groups.add(group_reg)
        user.save()

        login(self.request, user)
        new_user = Users(id_user=user)
        new_user.save()
        return redirect('main')



class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = "login_for_user.html"

    def get_success_url(self):
        return reverse_lazy("main")


class LoginSalesman(LoginView):
    form_class = AuthenticationForm
    template_name = "login_for_salesman.html"

    def get_success_url(self):
        return reverse_lazy("for_salesman")


class Search(ListView):
    model = Item
    template_name = 'search_result.html'
    context_object_name = 'items'

    def get_queryset(self):
        query = self.request.GET.get('search_name')
        object_list = Item.objects.filter(name=query)
        return object_list


class All_items(ListView):
    model = Item
    template_name = 'search_result.html'
    context_object_name = 'items'


class RegisterUser(CreateView):
    form_class = UserCreationForm
    template_name = "register_for_user.html"
    success_url = reverse_lazy("login")

    def form_valid(self, form):
        user = form.save()
        user.is_staff = True
        group_reg = Group.objects.get(name='user')
        user.groups.add(group_reg)
        user.save()

        login(self.request, user)
        new_basket = Basket.objects.create()
        new_basket.save()
        new_user = Users(id_user=user, basket=new_basket)
        new_user.save()
        return redirect('main')

    def form_invalid(self, form):
        raise ValueError
        # return redirect('add_user')


class RegisterSalesman(CreateView):
    form_class = UserCreationForm
    template_name = "register_for_salesman.html"
    success_url = reverse_lazy("login")

    def form_valid(self, form):
        user = form.save()
        user.is_staff = True
        group_reg = Group.objects.get(name='salesman')
        user.groups.add(group_reg)
        user.save()

        login(self.request, user)
        new_sale = Salesmans(id_user=user)
        new_sale.save()
        return redirect('for_salesman')


class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = "login_for_user.html"

    def get_success_url(self):
        return reverse_lazy("main")


def logout_user(request):
    logout(request)
    return redirect('main')
