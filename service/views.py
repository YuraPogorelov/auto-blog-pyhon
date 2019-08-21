from django.shortcuts import render
from .models import Category
from django.views.generic import ListView


class CategoryList(ListView):

    """список услуг по категориям"""

    model = Category
    queryset = Category.objects.all()
    context_object_name = 'categories'
    template_name = 'base.html'