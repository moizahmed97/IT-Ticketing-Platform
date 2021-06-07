from technicians.apps import TechniciansConfig
from django.urls import path
from .views import TechinicansListView

app_name = 'technicians'

urlpatterns = [
    path('', TechinicansListView.as_view(), name="technicians-list")
]