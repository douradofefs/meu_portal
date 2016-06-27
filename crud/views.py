from django.views.generic import  ListView, CreateView, DetailView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from .models import Element 


class ListElement(ListView):
	model = Element
	paginate_by = 100

class CreateElement(CreateView):
	model = Element
	fields = ('code', 'text')
	success_url = reverse_lazy('element_list')

class DetailElement(DetailView):
	model = Element 

class UpdateElement(UpdateView):
	model = Element
	fields = ('code', 'text')
	success_url = reverse_lazy('element_list')

class DeleteElement(DeleteView):
	model = Element
	success_url = reverse_lazy('element_list')
