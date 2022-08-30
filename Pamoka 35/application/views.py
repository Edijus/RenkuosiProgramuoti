from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import SignUpForm, EditUserAccountForm
from django.views.generic.list import ListView
from django.views.generic import View
from .models import Order
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView


# Create your views here.

class OrderBaseView(View):
    model = Order
    fields = '__all__'
    success_url = reverse_lazy('application:orders_all')


class RetrieveOrdersView(OrderBaseView, ListView):
    pass


class CreateOrderView(OrderBaseView, CreateView):
    pass


class UpdateOrderView(OrderBaseView, UpdateView):
    pass


class DeleteOrderView(OrderBaseView, DeleteView):
    pass


def index(request):
    return render(request, 'index.html')


def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index_test')
    else:
        form = SignUpForm()
    return render(request, 'registration/sign_up.html', context={'form': form})


def user_account(request):
    if request.method == 'POST':
        form = EditUserAccountForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('user_account')
    else:
        form = EditUserAccountForm(
            initial={
                'email': request.user.email,
                'image': request.user.image
            }
        )
    return render(request, 'user_account.html', context={'form': form})
