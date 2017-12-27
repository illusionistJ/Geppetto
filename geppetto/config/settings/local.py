from .base import *

print("[Geppetto] Local Setting Loading")

SECRET_KEY = os.environ.get('SECRET_KEY', os.urandom(32))

DEBUG = True

ALLOWED_HOSTS = ["127.0.0.1", "localhost"]

# STATICFILES_DIRS = [BASE_DIR.child("static"),]
