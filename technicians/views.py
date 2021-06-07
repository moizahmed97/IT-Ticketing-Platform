from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin


class TechinicansListView(LoginRequiredMixin, generic.ListView):
    template_name = "technicians/technician_list.html"