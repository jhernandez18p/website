from django.conf.urls import include, url
from django.contrib import admin

from local_apps.brand import views as brands_views
urlpatterns = [
    url(r'^$', brands_views.index, name='Brands'),
]
