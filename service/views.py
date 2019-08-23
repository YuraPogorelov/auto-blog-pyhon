from django.shortcuts import render
from .models import Category, Model
from django.views.generic import ListView


class CategoryList(ListView):

    """список услуг по категориям"""

    model = Category
    queryset = Category.objects.all()
    context_object_name = 'categories'
    template_name = 'base.html'


class ServiceModel(ListView):

    model = Model
    context_object_name = 'service_category'
    template_name = 'service/service_category.html'

    def get_queryset(self):
        return Model.objects.filter(category__slug=self.kwargs.get('slug'))