from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from issues.models import Technician


class TechinicansListView(LoginRequiredMixin, generic.ListView):
    template_name = "technicians/technicians_list.html"

    def get_queryset(self):
        return Technician.objects.all()