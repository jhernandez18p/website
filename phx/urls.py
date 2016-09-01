from django.conf.urls import url
from django.contrib import admin
from local_apps.frontend import views as front_views

urlpatterns = [
    url(r'^$', front_views.index, name='Home'),
    url(r'^phx/$', front_views.phx, name='PHX'),
    url(r'^quienes-somos/$', front_views.index, name='Who-We-Are'),
    url(r'^marcas/$', front_views.index, name='Brands'),
    url(r'^contact-mal/$', front_views.index, name='Contact-mail'),
    url(r'^admin/', admin.site.urls),
]
