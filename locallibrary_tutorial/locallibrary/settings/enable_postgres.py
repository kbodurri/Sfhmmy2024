from .settings import *

# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'locallibrary_db',
        'USER': 'admin',
        'PASSWORD': '1234',
        'HOST': 'postgres_db',
        'PORT': '5432',
    }
}
