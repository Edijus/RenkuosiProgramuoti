from django.shortcuts import render
from .models import Parent, Child


# Create your views here.

def index(request):
    request.session['my_data'] = 'my_value'  # saves value to session
    return render(request, 'index.html')


def show(request):
    my_data = request.session['my_data']  # read value back from session
    children = Parent.objects.values('child__name', 'child__code', 'child__date_created').all()
    parents = Child.objects.values('parent__name', 'parent__code', 'parent__date_created').distinct()
    context = {
        'parents': parents,
        'children': children
    }
    return render(request, 'show.html', context=context)
