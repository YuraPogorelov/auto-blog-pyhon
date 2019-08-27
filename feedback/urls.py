from django.urls import path
from .views import FeedBackFormView

urlpatterns = [
    path('', FeedBackFormView.as_view(), name='feedback_view')
]