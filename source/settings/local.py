# This is an example settings/local.py file.
# These settings overrides what's in settings/base.py

# To extend any settings from settings/base.py here's an example:
#from . import base
#INSTALLED_APPS = base.INSTALLED_APPS + ['debug_toolbar']

from os import environ as env

DATABASES = {
    'default': {
        'NAME': env.get("DATABASE_NAME","source_app.db"),
        'USER': env.get("DATABASE_USER",'mydatabaseuser'),
        'PASSWORD': env.get("DATABASE_PASSWORD",'mypassword'),
        'HOST': env.get("DATABASE_HOST",'127.0.0.1'),
        'PORT': env.get("DATABASE_PORT",'5432'),
    }
}

if 'DATABASE_NAME' in env:
   DATABASES['default']['ENGINE'] = 'django.db.backends.postgresql_psycopg2'
else:
    DATABASES['default']['ENGINE'] = 'django.db.backends.sqlite3'

    # 'slave': {
    #     ...
    # },


# Uncomment this and set to all slave DBs in use on the site.
# SLAVE_DATABASES = ['slave']

# Recipients of traceback emails and other notifications.
ADMINS = (
    # ('Your Name', 'your_email@domain.com'),
)
MANAGERS = ADMINS

GITHUB_CLIENT_ID = env.get("GITHUB_CLIENT_ID", "1234")

GITHUB_CLIENT_SECRET = env.get("GITHUB_CLIENT_SECRET","batmansecret")

# Debugging displays nice error messages, but leaks memory. Set this to False
# on all server instances and True only for development.
DEBUG = TEMPLATE_DEBUG = True

# Is this a development instance? Set this to True on development/master
# instances and False on stage/prod.
DEV = True

# # Playdoh ships with sha512 password hashing by default. Bcrypt+HMAC is safer,
# # so it is recommended. Please read <https://github.com/fwenzel/django-sha2#readme>,
# # then switch this to bcrypt and pick a secret HMAC key for your application.
PWD_ALGORITHM = 'bcrypt'

HMAC_KEYS = {}
for key in env.get('SOURCE_HMAC_KEYS', "2011-01-01|cheesecake").split(';'):
    (key_id, value) = key.split('|')
    HMAC_KEYS[key_id] = value

BASE_PASSWORD_HASHERS = (
    'django_sha2.hashers.BcryptHMACCombinedPasswordVerifier',
    'django_sha2.hashers.SHA512PasswordHasher',
    'django_sha2.hashers.SHA256PasswordHasher',
    'django.contrib.auth.hashers.SHA1PasswordHasher',
    'django.contrib.auth.hashers.MD5PasswordHasher',
    'django.contrib.auth.hashers.UnsaltedMD5PasswordHasher',
)

# Make this unique, and don't share it with anybody.  It cannot be blank.
SECRET_KEY = env.get("SECRET_KEY", "batman")

# Uncomment these to activate and customize Celery:
# CELERY_ALWAYS_EAGER = False  # required to activate celeryd
# BROKER_HOST = 'localhost'
# BROKER_PORT = 5672
# BROKER_USER = 'playdoh'
# BROKER_PASSWORD = 'playdoh'
# BROKER_VHOST = 'playdoh'
# CELERY_RESULT_BACKEND = 'amqp'

## Log settings

# SYSLOG_TAG = "http_app_playdoh"  # Make this unique to your project.
# LOGGING = dict(loggers=dict(playdoh={'level': logging.DEBUG}))

# Common Event Format logging parameters
#CEF_PRODUCT = 'Playdoh'
#CEF_VENDOR = 'Mozilla'

# Should robots.txt allow web crawlers?  Set this to True for production
ENGAGE_ROBOTS = True

if DEV:
    SESSION_COOKIE_SECURE = False

