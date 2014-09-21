#Login con Twitter utilizando Python Social Auth’s

Python Social Auth's es una libreria la cual nos permite trabajar con login's de las redes sociales mas populares del planeta en conjunto de una variedad de framework's de desarrollo.
En este caso se utilizara Twitter como proveedor y Django como framework de desarrollo.

#Instalación

Para poder instalar Python Social Auth’s, utilizaremos pip para descargar la libreria:

    $ pip install python-social-auth

Para poder utilizar Python Social Auth’s en nuestro poryecto, debemos incluirla en la lista de nuestras app's:

```
DJANGO_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

THIRD_PARTY_APPS = (
    'social.apps.django_app.default',
)

LOCAL_APPS = (
    'apps.system',
)

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS
```
