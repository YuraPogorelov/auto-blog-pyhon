from django.urls import path
from .views import CategoryList, ServiceModel

urlpatterns = [
    path('', CategoryList.as_view(), name='category_list'),
    path('<slug:slug>/', ServiceModel.as_view(), name='service_category')
]