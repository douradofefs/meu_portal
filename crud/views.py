from django.views.generic import CreateView, DetailView
from .models import Element 

class CreateElement(CreateView):
	model = Element
	fields = ('code', 'text')

class DetailElement(DetailView):
	model = Element 

