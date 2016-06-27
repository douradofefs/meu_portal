import requests
import random
from django.views.generic import  ListView, CreateView, DetailView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from .models import Element 
from .forms import ElementForm


class ListElement(ListView):
	model = Element
	paginate_by = 100

	def get_queryset(self):
		queryset = super(ListElement, self).get_queryset()
		q = self.request.GET.get('autocomplete')
		if q:
			queryset = queryset.filter(text__icontains=q)
		return queryset


	def get_context_data(self, **kwargs):
		context = super(ListElement, self).get_context_data(**kwargs)
		context['form'] = ElementForm()
		return context

def get_text_from_api():
	response = requests.get('http://api.randomuser.me/')
	if response.status_code == 200:
		js = response.json()
		return js.get('results')[0].get('location').get('street')
	return ''

def randomize():
	return random.randrange(100000)

class CreateElement(CreateView):
	model = Element
	fields = ('code', 'text')
	success_url = reverse_lazy('element_list')
	initial = {'code': randomize, 'text': get_text_from_api}

class DetailElement(DetailView):
	model = Element 

class UpdateElement(UpdateView):
	model = Element
	fields = ('code', 'text')
	success_url = reverse_lazy('element_list')

class DeleteElement(DeleteView):
	model = Element
	success_url = reverse_lazy('element_list')
