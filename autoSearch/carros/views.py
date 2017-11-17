# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView
from .models import Car
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .mixin import FormUserNeededMixin
from .form import CarModelForm
from django.db.models import Q
def home(request):
    return render(request, "home.html", context={"prueba":"esta es una prueba"})

class CarList(ListView):
    template_name = "car_list.html"
    queryset = Car.objects.all()
    # queryset = Tweet.objects.all()
    def get_queryset(self, *args, **kwargs):
        qs = Car.objects.all()
        print self.request.GET
        query = self.request.GET.get("q", None)
        if query is not None:
            qs = qs.filter(
                            Q(ttype__icontains=query) |
                            Q(year__icontains=query) |
                            Q(colour__icontains=query)
                          )
        return qs

    def get_context_data(self, *args, **kwargs):
        context = super(CarList, self).get_context_data(*args, **kwargs)
        print "Si llega aqui"
        context['create_form'] = CarModelForm()
        context['create_url'] = reverse_lazy("CarCreate")
        return context

class CarDetail(DetailView):
    template_name = "car_detail.html"
    queryset = Car.objects.all()
    def get_object(self):
        id = self.kwargs.get("id")
        print id
        return Car.objects.get(id=id)

class CarCreate(CreateView, LoginRequiredMixin, FormUserNeededMixin):
    form_class = CarModelForm
    template_name = "car/create_view.html"
    success_url = "/car"
    login_url = "/admin"

class CarDelete(DeleteView):
    model = Car
    template_name = "delete_view.html"
    success_url = reverse_lazy("car_list")

class CarUpdate(UpdateView):
    queryset = Car.objects.all()
    form_class = CarModelForm
    template_name = "update_view.html"
    success_url = "/car"
