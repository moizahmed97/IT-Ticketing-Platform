from django.shortcuts import render,reverse
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from issues.models import Technician
from .forms import TechnicianModelForm


class TechinicansListView(LoginRequiredMixin, generic.ListView):
    template_name = "technicians/technicians_list.html"

    def get_queryset(self):
        return Technician.objects.all()

class TechnicianCreateView(LoginRequiredMixin, generic.CreateView):
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


class TechnicianDetailView(LoginRequiredMixin, generic.DetailView):
    model = Technician 
    template_name = "technicians/technician_detail.html"        
    context_object_name = "technician"

class TechnicianDeleteView(LoginRequiredMixin, generic.DeleteView):
    template_name = "technicians/technician_delete_confirm.html"
    model = Technician
    def get_success_url(self):
        return reverse('technicians:technician-list')
