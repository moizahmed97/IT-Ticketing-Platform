from technicians.apps import TechniciansConfig
from django.urls import path
from .views import TechinicansListView, TechnicianCreateView,TechnicianDetailView, TechnicianDeleteView,TechnicianUpdateView

app_name = 'technicians'

urlpatterns = [
    path('', TechinicansListView.as_view(), name="technician-list"),
    path('create/', TechnicianCreateView.as_view(), name="technician-create"),
    path('<int:pk>/', TechnicianDetailView.as_view(), name="technician-detail"),
    path('<int:pk>/delete', TechnicianDeleteView.as_view(), name="technician-delete"),
    path('<int:pk>/update', TechnicianUpdateView.as_view(), name="technician-update")
]   