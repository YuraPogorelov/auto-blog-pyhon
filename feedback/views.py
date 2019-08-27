from django.shortcuts import render, redirect
from .forms import FeedBackForm
from django.views.generic import View


# Create your views here.
class FeedBackFormView(View):
    def post(self, request):
        form = FeedBackForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
