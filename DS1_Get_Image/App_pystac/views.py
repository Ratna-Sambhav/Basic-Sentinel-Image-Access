from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import CreateView, DetailView, ListView
from .models import Entries

# Create your views here.
class main(CreateView):
    model = Entries
    template_name = 'FrontPage.html'
    fields = '__all__'

class dataDetail(DetailView):
    model = Entries
    fields = '__all__'
    context_object_name = 'post'
    template_name = 'individual_entry.html'

class list(ListView):
    model = Entries
    template_name = 'AllEntries.html'
    context_object_name = 'entry'