# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Car
def home(request):
    return render(request, "home.html", context={"prueba":"esta es una prueba"})

class CarList(ListView):
    template_name = "car_list.html"
    queryset = Car.objects.all()

class CarDetail(DetailView):
    template_name = "car_detail.html"
    queryset = Car.objects.all()
    def get_object(self):
        id = self.kwargs.get("id")
        print id
        return Car.objects.get(id=id)
