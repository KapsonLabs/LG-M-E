from django.urls import path
from .views import DistrictListView, DistrictCreateView

urlpatterns = [
    path('districts/', DistrictListView.as_view(), name='district_list_view'),
    path('districts/create', DistrictCreateView.as_view(), name='district_create_view'),
]