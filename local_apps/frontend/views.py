# Django Imports
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse_lazy
from django.http import Http404, HttpResponse
from django.shortcuts import render
from django.views.generic import *
import datetime

# Apps Imports


def index(request):

    context = {
        'title': 'Home'
    }
    return render(request, 'frontend/index.html', context)

def home(request):
    now = datetime.datetime.now()
    # html = "<html><body>It is now %s.</body></html>" % now
    # return HttpResponse(html)
    return render(request, 'frontend/index.html', {
        'title': 'home',
        'sitename': 'Phoenix World Trade',
        'retail_brands':[{
                'name':'ALDO',
                'logo':'ALDO',
            },
            {
                'name':'BALU',
                'logo':'BALU',
            },
            {
                'name':'Charles',
                'logo':'Charles',
            },
            {
                'name':'MNG',
                'logo':'MNG',
            },
            {
                'name':'Parfois',
                'logo':'Parfois',
            },
            {
                'name':'Pronovias',
                'logo':'Pronovias',
            },
            {
                'name':'Rollerblade',
                'logo':'Rollerblade',
            },
            {
                'name':'Vestimenta',
                'logo':'Vestimenta',
            },
            {
                'name':'WomenSecret',
                'logo':'WomenSecret',
            },
            ],
        'wholesale_brands':[
            {
            'name':'DAKINE',
            'logo':'DAKINE',
            },
            {
            'name':'HH',
            'logo':'HH',
            },
            ],
    })
