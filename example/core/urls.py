from django.conf.urls import url

from .views import formset, advanced, index

urlpatterns = [
    url(r'^formset/', formset, name='example-formset'),
    url(r'^advanced/', advanced, name='example-advanced'),
    url(r'^', index, name='example-index'),
]
