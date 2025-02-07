
from datetime import timedelta
from pathlib import Path
from decouple import config
import dj_database_url
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', cast=bool)

ALLOWED_HOSTS = ["*"]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'authentication.apps.AuthenticationConfig',
    'orders.apps.OrdersConfig',
    'rest_framework',
    'phonenumber_field',
    'djoser',
    'rest_framework_simplejwt',
    'drf_yasg',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'pizza.urls'

AUTH_USER_MODEL ='authentication.User'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'pizza.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {}
if DEBUG:
     DATABASES['default']={
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
else:
    DATABASES['default'] = dj_database_url.config(conn_max_age=600, ssl_require=True)  
    DATABASES['default'] = dj_database_url.config(default=config('DATABASE_URL'))


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

REST_FRAMEWORK = {
    'NON_FIELD_ERRORS_KEY':'errors',
    'DEFAULT_AUTHENTICATION_CLASSES':[
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ]
}

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME':timedelta(hours=2),
    'REFRESH_TOKEN_LIFETIME':timedelta(hours=2),
    'ROTATE_REFRESH_TOKENS':False,
    'BLACKLIST_AFTER_ROTATION':False,
    'ALGORITH':'HS256',
    'SIGNING_KEY':SECRET_KEY,
    'VERIFYING_KEY':None,
    'AUDIENCE':None,
    'ISSUER':None,
    'JWT_URL':None,
    'LEEWAY':0,
    
    'AUTH_HEADER_TYPES':('Bearer',),
    'AUTH_HEADER_NAME':'HTTP_AUTHORIZATION',
    'USER_ID_FIELD':'id',
    'USER_ID_CLAIM':'user_id',
    'USER_AUTHENTICATION_RULE':'rest_framework_simplejwt.authentication.default_user_authentication_rule',
    
    # 'AUTH_TOKEN_CLASS':('rest_framework_simplejwt.tokens.AccessToken',),
    'TOKEN_TYPE_CLAIM':'token_type',
    'TOKEN_USER_CLASS':'rest_framework_simplejwt.models.TokenUser',
    'JTI_CLAIM':'jti',
    
    'SLIDING_TOKEN_REFRESH_EXP_CLAIM':'refresh_ep',
    'SLIDING_TOKEN_REFRESH_LIFETIME':timedelta(hours=2),
    'SLIDING_TOKEN_LIFETIME':timedelta(hours=2)
}

DJOSER = {
    'SEND_ACTIVATION_EMAIL': True,
    'ACTIVATION_URL':'auth/activate/{uid}/{token}',
    'PASSWORD_RESET_CONFIRM_URL':'password/reset/confirm/{uid}/{token}',
    'USERNAME_RESET_CONFIRM_URL':'username/reset/confirm/{uid}/{token}',
    'USER_CREATE_PASSWORD_RETYPE':False,
    'PASSWORD_RESET_CONFIRM_RETYPE':False,
    'PASSWORD_RESET_SHOW_EMAIL_NOT_FOUND':True,
    'SERIALIZERS':{
        'user_create':'authentication.serializer.UserSerializer',
        'user':'authentication.serializer.UserSerializer'
    }
}

# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / 'static'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
ALLOWED_HOSTS = ['*']

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = "olusegunoladipupo90@gmail.com"
EMAIL_HOST_PASSWORD = "wgjqyphavcyjsqmb"
# EMAIL_HOST_USER = config('EMAIL_HOST_USER')
# EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')
SWAGGER_SETTINGS = {
    'SECURITY_DEFINITIONS':{
        'Bearer':{
            'type':'apiKey',
            'name':'Authorization',
           'in':'header' 
        }
    }
}

MAILJET_API_KEY= '3a565a9e70e77c5082bdb2e69b4689db'
MAILJET_API_SECRET='614181d140e96a3c38ffe493ab134148'