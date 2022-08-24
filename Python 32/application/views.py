from django.shortcuts import render, redirect, reverse
from .models import Order, OrderDetail
from django.core.paginator import Paginator
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required, permission_required
from django.db.models import F, Sum
from .forms import SignUpForm, CreateOrderForm, CreateOrderDetailForm


# Create your views here.

def index(request):
    return render(request, 'index.html')


@permission_required('application.can_see_all_orders')
@login_required()
def show_orders(request, page=1):
    orders_per_page = 10
    orders = Order.objects \
        .annotate(order_detail_price=F('orderdetail__quantity') * F('orderdetail__service__price')) \
        .annotate(total_price=Sum('order_detail_price')).order_by('-date_created') \
        .values('id', 'image', 'date_created', 'total_price', 'vehicle')
    paginator = Paginator(orders, orders_per_page)
    paginated_orders = paginator.get_page(page)
    context = {
        'orders': paginated_orders
    }
    return render(request, 'show_orders.html', context=context)


@login_required()
def show_user_orders(request, page=1):
    orders_per_page = 5
    orders = Order.objects.filter(user=request.user.id) \
        .annotate(order_detail_price=F('orderdetail__quantity') * F('orderdetail__service__price')) \
        .annotate(total_price=Sum('order_detail_price')).order_by('-date_created') \
        .values('id', 'image', 'date_created', 'total_price', 'vehicle')
    paginator = Paginator(orders, orders_per_page)
    paginated_orders = paginator.get_page(page)
    context = {
        'orders': paginated_orders
    }
    return render(request, 'show_orders.html', context=context)


def show_order(request, id):
    order_details = OrderDetail.objects.filter(order=id).annotate(price=F('quantity') * F('service__price')).all()
    context = {
        'order_details': order_details
    }
    return render(request, 'show_order.html', context=context)


def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(reverse('index'))
    else:
        form = SignUpForm()
    return render(request, 'registration/sign_up.html', context={'form': form})


def create_order(request):
    if request.method == 'POST':
        request_data = request.POST.copy()
        request_data['user'] = request.user.id
        form = CreateOrderForm(request_data, request.FILES)
        if form.is_valid():
            order = form.save()
            return redirect(f'/create_order_detail{order.id}/')
    else:
        form = CreateOrderForm()
    return render(request, 'create_order.html', context={'form': form})


def create_order_detail(request, id):
    if request.method == 'POST':
        request_data = request.POST.copy()
        request_data['order'] = id
        form = CreateOrderDetailForm(request_data)
        if form.is_valid():
            order = form.save()
            return redirect(f'/create_order_detail{id}/')
    else:
        form = CreateOrderDetailForm(initial={'order': Order.objects.get(id=id)})
    return render(request, 'create_order_detail.html', context={'form': form})