from technicians.apps import TechniciansConfig
from django.urls import path
from .views import IssuerListView, IssuerCreateView,IssuerDetailView, IssuerDeleteView

app_name = 'issuers'

urlpatterns = [
    path('', IssuerListView.as_view(), name="technician-list"),
    path('create/', IssuerCreateView.as_view(), name="technician-create"),
    path('<int:pk>/', IssuerDetailView.as_view(), name="technician-detail"),
    path('<int:pk>/delete', IssuerDeleteView.as_view(), name="technician-delete")
]   