from django.shortcuts import render, redirect, reverse
from .models import Order, OrderDetail
from django.core.paginator import Paginator
from django.db.models import F, Sum
from .forms import SignUpForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required


# Create your views here.

def index(request):
    return render(request, 'index.html')


@login_required()
def show_orders(request, page=1):
    orders_per_page = 1
    orders = Order.objects.annotate(order_detail_sum=F('orderdetail__quantity') * F('orderdetail__service__price')).\
        annotate(total_sum=Sum('order_detail_sum')).order_by('-date_created').\
        values('id', 'image', 'date_created', 'total_sum', 'vehicle')
    paginator = Paginator(orders, orders_per_page)
    paginated_orders = paginator.get_page(page)
    context = {
        'orders': paginated_orders
    }
    return render(request, 'show_orders.html', context=context)


def show_order(request, id):
    order_details = OrderDetail.objects.filter(order=id).annotate(sum=F('quantity') * F('service__price')).all()
    context = {
        'order_details': order_details
    }
    return render(request, 'show_order.html', context=context)


def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(reverse('index'))
    else:
        form = SignUpForm()
    return render(request, 'registration/sign_up.html', context={'form': form})
