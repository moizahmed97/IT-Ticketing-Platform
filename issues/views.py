from django.contrib.auth import login
from django.db.models import query
from django.shortcuts import render
from django.views import generic
from issues.models import Issue,Issuer
from .forms import CustomUserCreationForm
from django.shortcuts import render,reverse,redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from issuers.mixins import AdminAndIssuerMixin



class SignUpView(generic.CreateView):
    template_name = "registration/signup.html"
    form_class = CustomUserCreationForm

    def get_success_url(self):
        return reverse("login")

class IssueListView(LoginRequiredMixin, generic.ListView):
    template_name="issue_list.html"
    context_object_name="issues"

    # Get different data depending on the type of the user 
    def get_queryset(self):
        user = self.request.user 
        if user.is_superuser:
            queryset = Issue.objects.all()
        else:
            queryset = Issue.objects.filter(issuer__user=user)  # Filters Issues where the issuer is the current user (ie issuer)
            # we can do issuer = user since we can only equate issuer to issuer
            # there issuer_user is a bit like issuer -> user
        return queryset


    # Update the context so we can display the unassigned issues
    def get_context_data(self, **kwargs):
        context = super(IssueListView, self).get_context_data(**kwargs)
        user = self.request.user
        # Only update the context for unassigned issues if the user is admin 
        if user.is_superuser:
            context.update({
                "unassigned_issues" : Issue.objects.filter(technician__isnull = True)
            })
        return context

class IssueDetailView(LoginRequiredMixin, generic.DetailView):
    template_name = "issues/issue_detail.html"
    model = Issue
    context_object_name = "issue"
    

class IssueCreateView(LoginRequiredMixin, generic.CreateView):
    model = Issue
    # The class view automatically expects a template by the name of issue_form in the templates/issues folder
    fields = ['issue_type', 'issue_detail', 'priority', 'location']

    def form_valid(self, form):
         # Attach the issuer ID to the form submission
        form.instance.issuer = Issuer.objects.get(user=self.request.user)
        return super().form_valid(form)
        
    def get_success_url(self):
        return  reverse("issues:issue-list") 

class IssueUpdateView(AdminAndIssuerMixin, generic.UpdateView):
    model = Issue
    # The class view automatically expects a template by the name of issue_form in the templates/issues folder
    fields = ['issue_type', 'issue_detail']

    def form_valid(self, form):
        # Attach the issuer ID to the form submission 
        form.instance.issuer = Issuer.objects.get(user=self.request.user)
        return super().form_valid(form)
        
    def get_success_url(self):
        return  reverse("issues:issue-list") 

class IssueDeleteView(AdminAndIssuerMixin, generic.DeleteView):
    model = Issue      
    def get_success_url(self):
        return  reverse("issues:issue-list")       


class LandingPageView(generic.TemplateView):
    template_name = "landing.html"
