#Urls de app landing
from django.conf.urls import url
from .views import index,agregar,detalle, some

urlpatterns = [
    url(r'^$',index, name="index"),
    url(r'^agregar/$',agregar, name="agregar"),
    url(r'^detalle/(?P<pk>[0-9]+)/$', detalle, name="detalle"),
    url(r'^some/', some, name="some")
]