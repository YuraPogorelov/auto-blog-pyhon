from django.shortcuts import render
from .models import Category, Model
from django.views.generic import ListView, DetailView


class CategoryList(ListView):

    """список услуг по категориям"""

    model = Category
    queryset = Category.objects.all()
    context_object_name = 'categories'
    template_name = 'base.html'


class ServiceModel(ListView):

    """список услуг по категориям"""

    model = Model
    context_object_name = 'service_category'
    template_name = 'service/service_category.html'

    def get_queryset(self):
        return Model.objects.filter(category__slug=self.kwargs.get('slug'))


class ServiceModelView(DetailView):

    """Отображение услуги из категории"""

    model = Model
    context_object_name = 'service_model_view'
    template_name = 'service/service_model.html'

    def get_queryset(self):
        return Model.objects.filter(category__slug=self.kwargs.get('category'), slug=self.kwargs.get('slug'))
