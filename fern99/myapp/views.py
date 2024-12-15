
from django.shortcuts import render
from .models import course
# Create your views here.
from .models import *
from django.urls import reverse_lazy
from django.views.generic import *

def C(request):
    name = request.GET.get("name", "")
    c = course.objects.filter(name=name)
    return render(request, "c.html", {"c": c})