from django.urls import path
from .views import CategoryList, ServiceModel, ServiceModelView

urlpatterns = [
    path('', CategoryList.as_view(), name='category_list'),
    path('<slug:slug>/', ServiceModel.as_view(), name='service_category'),
    path('<slug:category>/<slug:slug>/', ServiceModelView.as_view(), name='service_model_view'),
]
