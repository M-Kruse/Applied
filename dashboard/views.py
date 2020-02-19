from django.shortcuts import render
from django.views import generic

# Create your views here.
class DashboardIndexView(generic.ListView):
    template_name = 'dashboard/index.html'
    context_object_name = 'dashboard_list'

    def get_queryset(self):
        return None