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

# Create your views here.
def index(request):
    now = datetime.datetime.now()
    # html = "<html><body>It is now %s.</body></html>" % now
    # return HttpResponse(html)

    brands ={'retail':[
        {
            'id':1,
            'name':'ALDO',
            'logo':'ALDO',
            'cat':'dbcwkebfk',
            'desc':'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.',
            'brand_url':'phoenixworldtrade.com',
            'redes_sociales':[{
                'facebook':'/phoenixworldtrade',
                'instagram':'@phoenixworldtrade',
                'twitter':'@phoenixworldtrade',
            }],
            'tags':'',
            'paises':'Panama;Venezuela;Republica Dominicana;Puerto Rico;Peru;',
        },
        {
            'id':2,
            'name':'BALU',
            'logo':'BALU',
            'cat':'dbcwkebfk',
            'desc':'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.',
            'brand_url':'phoenixworldtrade.com',
            'redes_sociales':[{
                'facebook':'/phoenixworldtrade',
                'instagram':'@phoenixworldtrade',
                'twitter':'@phoenixworldtrade',
            }],
            'tags':'',
            'paises':'Panama;Venezuela;Republica Dominicana;Puerto Rico;Peru;',
        },
        {
            'id':3,
            'name':'Charles',
            'logo':'Charles',
            'cat':'dbcwkebfk',
            'desc':'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.',
            'brand_url':'phoenixworldtrade.com',
            'redes_sociales':[{
                'facebook':'/phoenixworldtrade',
                'instagram':'@phoenixworldtrade',
                'twitter':'@phoenixworldtrade',
            }],
            'tags':'',
            'paises':'Panama;Venezuela;Republica Dominicana;Puerto Rico;Peru;',
        },
        {
            'id':4,
            'name':'MNG',
            'logo':'MNG',
            'cat':'dbcwkebfk',
            'desc':'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.',
            'brand_url':'phoenixworldtrade.com',
            'redes_sociales':[{
                'facebook':'/phoenixworldtrade',
                'instagram':'@phoenixworldtrade',
                'twitter':'@phoenixworldtrade',
            }],
            'tags':'',
            'paises':'Panama;Venezuela;Republica Dominicana;Puerto Rico;Peru;',
        },
        {
            'id':5,
            'name':'Parfois',
            'logo':'Parfois',
            'cat':'dbcwkebfk',
            'desc':'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.',
            'brand_url':'phoenixworldtrade.com',
            'redes_sociales':[{
                'facebook':'/phoenixworldtrade',
                'instagram':'@phoenixworldtrade',
                'twitter':'@phoenixworldtrade',
            }],
            'tags':'',
            'paises':'Panama;Venezuela;Republica Dominicana;Puerto Rico;Peru;',
        },
        {
            'id':6,
            'name':'Pronovias',
            'logo':'Pronovias',
            'cat':'dbcwkebfk',
            'desc':'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.',
            'brand_url':'phoenixworldtrade.com',
            'redes_sociales':[{
                'facebook':'/phoenixworldtrade',
                'instagram':'@phoenixworldtrade',
                'twitter':'@phoenixworldtrade',
            }],
            'tags':'',
            'paises':'Panama;Venezuela;Republica Dominicana;Puerto Rico;Peru;',
        },
        {
            'id':7,
            'name':'Rollerblade',
            'logo':'Rollerblade',
            'cat':'dbcwkebfk',
            'desc':'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.',
            'brand_url':'phoenixworldtrade.com',
            'redes_sociales':[{
                'facebook':'/phoenixworldtrade',
                'instagram':'@phoenixworldtrade',
                'twitter':'@phoenixworldtrade',
            }],
            'tags':'',
            'paises':'Panama;Venezuela;Republica Dominicana;Puerto Rico;Peru;',
        },
        {
            'id':8,
            'name':'Vestimenta',
            'logo':'Vestimenta',
            'cat':'dbcwkebfk',
            'desc':'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.',
            'brand_url':'phoenixworldtrade.com',
            'redes_sociales':[{
                'facebook':'/phoenixworldtrade',
                'instagram':'@phoenixworldtrade',
                'twitter':'@phoenixworldtrade',
            }],
            'tags':'',
            'paises':'Panama;Venezuela;Republica Dominicana;Puerto Rico;Peru;',
        },
        {
            'id':9,
            'name':'WomenSecret',
            'logo':'WomenSecret',
            'cat':'dbcwkebfk',
            'desc':'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.',
            'brand_url':'phoenixworldtrade.com',
            'redes_sociales':[{
                'facebook':'/phoenixworldtrade',
                'instagram':'@phoenixworldtrade',
                'twitter':'@phoenixworldtrade',
            }],
            'tags':'',
            'paises':'Panama;Venezuela;Republica Dominicana;Puerto Rico;Peru;',
        },],
    'wholesale':[
            {
                'id':1,
                'name':'DAKINE',
                'logo':'DAKINE',
                'cat':'dbcwkebfk',
                'desc':'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.',
                'brand_url':'phoenixworldtrade.com',
                'redes_sociales':[{
                    'facebook':'/phoenixworldtrade',
                    'instagram':'@phoenixworldtrade',
                    'twitter':'@phoenixworldtrade',
                }],
                'tags':'',
                'paises':'Panama;Venezuela;Republica Dominicana;Puerto Rico;Peru;',
            },
            {
                'id':2,
                'name':'HH',
                'logo':'HH',
                'cat':'dbcwkebfk',
                'desc':'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.',
                'brand_url':'phoenixworldtrade.com',
                'redes_sociales':[{
                    'facebook':'/phoenixworldtrade',
                    'instagram':'@phoenixworldtrade',
                    'twitter':'@phoenixworldtrade',
                }],
                'tags':'',
                'paises':'Panama;Venezuela;Republica Dominicana;Puerto Rico;Peru;',
            },
        ],
    }

    return render(request, 'frontend/brands.html', {'title': 'home','sitename': 'Phoenix World Trade','brands': brands,})
