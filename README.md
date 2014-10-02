# Login con Twitter utilizando Python Social Auth’s

Python Social Auth's es una libreria la cual nos permite trabajar con login's de las redes sociales mas populares del planeta en conjunto de una variedad de framework's de desarrollo.
En este caso se utilizara Twitter como proveedor y Django como framework de desarrollo.

### Instalación

Para poder instalar Python Social Auth’s, utilizaremos pip para descargar la libreria:

    $ pip install python-social-auth

Para poder utilizar Python Social Auth’s en nuestro proyecto, debemos incluirla en la lista de nuestras app's:

    
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
    
---    
Una vez registrada la app , es hora de sincronizar la base de datos para que la libreria cree las tablas necesarias para su funcionamiento:

    $ ./manage.py syncdb

### Configuración

Twitter nos van a pedir dos códigos, un API_KEY y un API_SECRET. Esto es lo primero que se debe *setear* en nuestro *settings.py*.

#### Twitter

Para que nuestros usuarios se puedan *loguear* con Twitter debemos crear una aplicación. <https://dev.twitter.com/apps/new>. Y añadir las llaves de nuestra aplicación(Twitter) en *settings.py*.

```
SOCIAL_AUTH_TWITTER_KEY = 'mi-consumer-key-de-twitter'
SOCIAL_AUTH_TWITTER_SECRET = 'mi-consumer-secret-de-twitter'
```

##### Importante

![Alt text](https://scontent-a-mia.xx.fbcdn.net/hphotos-xfp1/t31.0-8/10428200_875021005848868_145073369195948334_o.png?raw=true "Optional Title")

Se necesita definir un url en el callback , la cual tiene que ser la direccion que se desea ir si el *login* se realizo correctamente.

### Backends

Ahora necesitamos especificar que *backends* o redes sociales usaremos en *settings.py*.

```
AUTHENTICATION_BACKENDS = (
    'social.backends.twitter.TwitterOAuth',
    ...
    'django.contrib.auth.backends.ModelBackend',
)
```

**Importante**

Si no incluímos ``'django.contrib.auth.backends.ModelBackend'`` al final de nuestros *backends*, los usuarios no podrán *loguearse* con usuario y contraseña.

### URLs

Necesitamos agregar las urls que utilizaremos en este caso. Para nuestro ejemplo usaremos **dos** en *settings.py*. Exite una gran variedad que podemos revisar en la documentacion oficial.

```
SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/home/'
SOCIAL_AUTH_LOGIN_URL = '/'
```

De igual manera a esto tenemos que habilitar las URLs con las que vamos a *loguear* a los usuarios. Esto se hace en *urls.py*.

	url('', include('social.apps.django_app.urls', namespace='social'))

### Template

Al final sólo nos resta colocar el enlace para que nuestros usuarios se puedan *loguear* con Twitter.

```
<a href="{% url 'social:begin' 'twitter' %}">Twitter</a>
```

# Demo

Para poder probar la **demo** solo necesitamos bajar el repositorio de github.
- Una vez tengamos el repositorio, necesitamos instalar Python Social Auth's
- Luego accedemos por linea de comando y ejecutamos *syncdb*
- Ahora necesitamos agregar las api´key´s de nuestra aplicación en Twitter en nuestro archivo **setting.py**
- Una vez configurado el proyecto , arrancamos el servidor y a probar la demo


### Documentacion Oficial

Para poder logrer el uso de otras funciones de Python Social Auth's podemos revisar la documentacion oficial y ver los proveedores que dispone y todo lo que podemos lograr con esta espectacular libreria.

[Documentacion Oficial](http://python-social-auth.readthedocs.org/en/latest/)
