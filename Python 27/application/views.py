from django.shortcuts import render
from .models import Parent, Child
from django.http import HttpResponse
from django.views import View
from django.views.generic import ListView


# Create your views here.

class Index(View):
    template_name = 'index.html'

    def get(self, request):
        return render(request, self.template_name)


# def show(request):
#     children = Parent.objects.values('child__name', 'child__code', 'child__date_created').all()
#     parents = Child.objects.values('parent__name', 'parent__code', 'parent__date_created').distinct()
#     context = {
#         'parents': parents,
#         'children': children
#     }
#     return render(request, 'show.html', context=context)

class Show(ListView):
    # model = Child
    queryset = Child.objects.values('parent__name', 'parent__code', 'parent__date_created').distinct()
    context_object_name = 'parents'
    template_name = 'show.html'
