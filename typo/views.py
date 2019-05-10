from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.views import generic

class IndexView(generic.ListView):
    template_name = 'typo/index.html'
	
    def get_queryset(self):
        """Return the last five published questions."""
        return "hello"

# Create your views here.
