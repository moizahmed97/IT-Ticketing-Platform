from django.shortcuts import render,reverse
from django.views import generic
from issues.models import Issue, Issuer
from .forms import IssuerModelForm
from issuers.mixins import AdminAndLoginRequiredMixin



class IssuerListView(AdminAndLoginRequiredMixin, generic.ListView):
    template_name = "issuers/issuers_list.html"

    def get_queryset(self):
        return Issuer.objects.all()

class IssuerCreateView(AdminAndLoginRequiredMixin, generic.CreateView):
    template_name="issuers/issuer_form.html"
    form_class = IssuerModelForm

    def form_valid(self, form):
        user = form.save(commit=False) 
        user.is_issuer = True
        user.set_password("!Qaz2wsx")
        user.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('issuers:issuers-list')    


class IssuerDetailView(AdminAndLoginRequiredMixin, generic.DetailView):
    model = Issuer 
    template_name = "issuers/issuer_detail.html"        
    context_object_name = "issuer"

class IssuerDeleteView(AdminAndLoginRequiredMixin, generic.DeleteView):
    template_name = "issuers/issuer_delete_confirm.html"
    model = Issuer
    def get_success_url(self):
        return reverse('issuers:issuers-list')

