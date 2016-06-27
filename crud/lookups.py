from __future__ import unicode_literals

from selectable.base import ModelLookup
from selectable.registry import registry

from .models import Element


class ElementLookup(ModelLookup):
    model = Element
    search_fields = ('text__icontains', )

registry.register(ElementLookup)
