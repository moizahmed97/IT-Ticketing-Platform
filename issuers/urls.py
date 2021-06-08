from technicians.apps import TechniciansConfig
from django.urls import path
from .views import IssuerListView, IssuerCreateView,IssuerDetailView, IssuerDeleteView

app_name = 'issuers'

urlpatterns = [
    path('', IssuerListView.as_view(), name="issuers-list"),
    path('create/', IssuerCreateView.as_view(), name="issuer-create"),
    path('<int:pk>/', IssuerDetailView.as_view(), name="issuer-detail"),
    path('<int:pk>/delete', IssuerDeleteView.as_view(), name="issuer-delete")
]   