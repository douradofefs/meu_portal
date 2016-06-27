from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from .models import Element 

class CreateElement(CreateView):
	model = Element
	fields = ('code', 'text')

class DetailElement(DetailView):
	model = Element 

class UpdateElement(UpdateView):
	model = Element
	fields = ('code', 'text')

class DeleteElement(DeleteView):
	model = Element

