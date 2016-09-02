# Django Imports
from decouple import config
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import send_mail
from django.core.urlresolvers import reverse_lazy
from django.http import Http404, HttpResponse
from django.shortcuts import render
from django.views.generic import *
import datetime
import json

# Apps Imports


def index(request):

    context = {
        'title': 'Home'
    }
    return render(request, 'frontend/building-it.html', context)

def contact(request):

    if request.method == 'GET':

        return render(request, 'frontend/building-it.html',{'title':'Home'})

    elif request.method == 'POST':

        name = request.POST['name']
        email = request.POST['email']
        comments = request.POST['comments']

        if name == '':

            return render(request, 'frontend/building-it.html',{'title':'Home'})

        elif email == '':

            return render(request, 'frontend/building-it.html',{'title':'Home'})

        elif comments == '':

            return render(request, 'frontend/building-it.html',{'title':'Home'})

        send_mail(
		            'Email de contato, página web',
		            '%s, ha estado visitando la página web. Su email es: %s, nos ha dejado el siguiente mensaje. \n %s' % (name,email,comments) ,
		            config("WEBSITE_EMAIL_HOST_USER",),
		            [config("WEBSITE_EMAIL_HOST_USER",)],
		            fail_silently=False,
		        )

        context = {
            'title': 'Home'
        }
        return render(request, 'frontend/index.html', context)

def phx(request):

    context = {
        'title': 'Home'
    }
    return render(request, 'frontend/index.html', context)


def who_we_are(request):
    locations ={"paises":[
            {
                "name":"Venezuela",
                "lat":"440",
                "long":"465",
                "desc":"ckjnkjvns"
            },{
                "name":"Panamá",
                "lat":"380",
                "long":"440",
                "desc":""
            },{
                "name":"Colombia",
                "lat":"408",
                "long":"455",
                "desc":""
            },{
                "name":"Chile",
                "lat":"425",
                "long":"595",
                "desc":""
            },{
                "name":"Perú",
                "lat":"395",
                "long":"505",
                "desc":""
            },{
                "name":"Ecuador",
                "lat":"385",
                "long":"475",
                "desc":""
            },{
                "name":"Brasil",
                "lat":"505",
                "long":"505",
                "desc":""
            },{
                "name":"Costa Rica",
                "lat":"370",
                "long":"435",
                "desc":""
            },{
                "name":"República Dominicana",
                "lat":"420",
                "long":"402",
                "desc":""
            },{
                "name":"Aruba",
                "lat":"428",
                "long":"427",
                "desc":""
            },{
                "name":"St. Maarten",
                "lat":"448",
                "long":"406",
                "desc":""
            },{
                "name":"Puerto Rico",
                "lat":"436",
                "long":"406",
                "desc":""
            },{
                "name":"Curacao",
                "lat":"432",
                "long":"427",
                "desc":""
            },{
                "name":"EEUU",
                "lat":"384",
                "long":"375",
                "desc":""
            }
        ]}
    timeline = {
        'dates' :[
            {
                'id':1,
                'name':'La Gran Familia',
                'fecha':'1972',
                'title':'Caracas',
                'desc':'La Gran Familia empieza su negocio de retail con su primera tienda en Colombia ubicada en la frontera con Venezuela.',
                'position':'left',
            },{
                'id':2,
                'name':'La Compañia se Muda',
                'fecha':'1978',
                'title':'Margarita',
                'desc':'La compañíase muda a Margarita, donde las condiciones para importar favorecen el crecimiento de la representación de marcas internacionales.',
                'position':'timeline-inverted',
            },{
                'id':3,
                'name':'La Gran Familia',
                'fecha':'19980',
                'title':'Margarita',
                'desc':'La Gran Familia adquiere en el territorio la subdistribución de las marcas deportivas NIKE, PUMA, CONVERSE y PONY.',
                'position':'left',
            },{
                'id':4,
                'name':'Apertura de la primera tienda retail',
                'fecha':'1990',
                'title':'Margarita',
                'desc':'Apertura de la primera tienda retail: PLANETA SPORT. El grupo se convierte en distribuidor autorizado de TIMBERLAND.',
                'position':'timeline-inverted',
            }
        ]
    }
    context = {
        'title': 'Home',
        'locations':locations,
        'timeline':timeline,
    }
    return render(request, 'frontend/whoweare.html', context)
