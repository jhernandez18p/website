from phx.settings.base import *


SECRET_KEY = config('WEBSITE_SECRET_KEY')

DEBUG = config('WEBSITE_DEBUG',default=False, cast=bool)

ALLOWED_HOSTS = ['intra.phoenixworldtrade.com']

# AUTH_USER_MODEL = 'intra_profile.User'

DATABASES ={
            'default':{
                'ENGINE': 'django.db.backends.postgresql',
                'NAME': config('WEBSITE_DB_NAME'),
                'USER': config('WEBSITE_DB_USER'),
                'PASSWORD': config('WEBSITE_DB_PASSWORD'),
                'HOST': config('WEBSITE_DB_HOST'),
                'PORT': config('WEBSITE_DB_PORT',cast=int),
                }
            }
