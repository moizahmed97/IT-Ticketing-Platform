from django.contrib.auth import login
from django.shortcuts import render
from django.views import generic
from issues.models import Issue,Issuer
from .forms import CustomUserCreationForm
from django.shortcuts import render,reverse,redirect
from django.contrib.auth.mixins import LoginRequiredMixin


class SignUpView(generic.CreateView):
    template_name = "registration/signup.html"
    form_class = CustomUserCreationForm

    def get_success_url(self):
        return reverse("login")

class IssueListView(LoginRequiredMixin, generic.ListView):
    template_name="issue_list.html"
    context_object_name="issues"
    model = Issue    

class IssueDetailView(LoginRequiredMixin, generic.DetailView):
    template_name = "issues/issue_detail.html"
    model = Issue
    context_object_name = "issue"
    

class IssueCreateView(LoginRequiredMixin, generic.CreateView):
    model = Issue
    # The class view automatically expects a template by the name of issue_form in the templates/issues folder
    fields = ['issue_type', 'issue_detail']

    def form_valid(self, form):
         # Attach the issuer ID to the form submission
        form.instance.issuer = Issuer.objects.get(user=self.request.user)
        return super().form_valid(form)
        
    def get_success_url(self):
        return  reverse("issues:issue-list") 

class IssueUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Issue
    # The class view automatically expects a template by the name of issue_form in the templates/issues folder
    fields = ['issue_type', 'issue_detail']

    def form_valid(self, form):
        # Attach the issuer ID to the form submission 
        form.instance.issuer = Issuer.objects.get(user=self.request.user)
        return super().form_valid(form)
        
    def get_success_url(self):
        return  reverse("issues:issue-list") 

class IssueDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Issue      
    def get_success_url(self):
        return  reverse("issues:issue-list")       


class LandingPageView(generic.TemplateView):
    template_name = "landing.html"
