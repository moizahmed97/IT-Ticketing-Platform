from django.shortcuts import render,reverse
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from issues.models import Issue, Issuer
from .forms import TechnicianModelForm


class IssuerListView(LoginRequiredMixin, generic.ListView):
    template_name = "issuers/issuer_list.html"

    def get_queryset(self):
        return Issue.objects.all()

class IssuerCreateView(LoginRequiredMixin, generic.CreateView):
    template_name="issuers/issuer_form.html"
    form_class = TechnicianModelForm

    def form_valid(self, form):
        user = form.save(commit=False) 
        user.is_technician = True
        user.set_password("!Qaz2wsx")
        user.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('issuers:issuer-list')    


class IssuerDetailView(LoginRequiredMixin, generic.DetailView):
    model = Issuer 
    template_name = "issuers/issuer_detail.html"        
    context_object_name = "issuer"

class IssuerDeleteView(LoginRequiredMixin, generic.DeleteView):
    template_name = "issuers/issuer_delete_confirm.html"
    model = Issuer
    def get_success_url(self):
        return reverse('issuers:issuers-list')

