from django import forms

from selectable.forms import AutoCompleteWidget

from .lookups import ElementLookup


class ElementForm(forms.Form):
    autocomplete = forms.CharField(
        label='Digite o que deseja buscar:',
        widget=AutoCompleteWidget(ElementLookup),
        required=False,
    )
