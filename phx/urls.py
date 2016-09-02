from django.conf.urls import include, url
from django.contrib import admin

from local_apps.frontend import views as front_views

urlpatterns = [
    url(r'^$', front_views.index, name='Home'),
    url(r'^phx/$', front_views.phx, name='PHX'),
    url(r'^quienes-somos/$', front_views.who_we_are, name='Who-We-Are'),
    url(r'^marcas/$', include('local_apps.brand.urls')),
    url(r'^contacto/$', front_views.contact, name='Contact-mail'),
    url(r'^admin/', admin.site.urls),
]
