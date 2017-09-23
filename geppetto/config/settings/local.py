from .base import *

print("Local Setting Loading")

SECRET_KEY = os.environ.get('SECRET_KEY', os.urandom(32))

DEBUG = True

ALLOWED_HOSTS = ["127.0.0.1", "localhost"]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}