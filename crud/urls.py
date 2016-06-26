from django.conf.urls import include, url
from .views import CreateElement

urlpatterns = [
    url(r'^element/new/$', CreateElement.as_view(), name='element_new'),
]