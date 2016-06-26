from django.views.generic import CreateView
from .models import Element 

class CreateElement(CreateView):
	model = Element
	fields = ('code', 'text')
