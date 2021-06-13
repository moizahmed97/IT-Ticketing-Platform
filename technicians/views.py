from django.shortcuts import render,reverse
from django.views import generic
from issues.models import Technician
from .forms import TechnicianModelForm
from issuers.mixins import AdminAndLoginRequiredMixin


class TechinicansListView(AdminAndLoginRequiredMixin, generic.ListView):
    template_name = "technicians/technicians_list.html"

    def get_queryset(self):
        return Technician.objects.all()

class TechnicianCreateView(AdminAndLoginRequiredMixin, generic.CreateView):
    template_name="technicians/technician_form.html"
    form_class = TechnicianModelForm

    def form_valid(self, form):
        user = form.save(commit=False) 
        user.is_technician = True
        user.set_password("!Qaz2wsx")
        user.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('technicians:technician-list')    


class TechnicianDetailView(AdminAndLoginRequiredMixin, generic.DetailView):
    model = Technician 
    template_name = "technicians/technician_detail.html"        
    context_object_name = "technician"

class TechnicianDeleteView(AdminAndLoginRequiredMixin, generic.DeleteView):
    template_name = "technicians/technician_delete_confirm.html"
    model = Technician
    def get_success_url(self):
        return reverse('technicians:technician-list')


class TechnicianUpdateView(AdminAndLoginRequiredMixin, generic.UpdateView):
    template_name = "technicians/technician_update.html"
    form_class = TechnicianModelForm

    def get_success_url(self):
        return reverse("technicians:technician-list")

    def get_queryset(self):
        return Technician.objects.all()

