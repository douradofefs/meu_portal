from django.conf.urls import include, url
from .views import CreateElement, DetailElement, UpdateElement

urlpatterns = [
    url(r'^element/new/$', CreateElement.as_view(), name='element_new'),
	url(r'^element/(?P<pk>[0-9]+)/$', DetailElement.as_view(), name='element_detail'),
	url(r'^element/edit/(?P<pk>[0-9]+)/$', UpdateElement.as_view(), name='element_update'),
]
