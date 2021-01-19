import os

from django.core.wsgi import get_wsgi_application

# Set PRODUCTION_ENV=1 in heroku production environment to use production settings
if os.environ.get("PRODUCTION_ENV"):
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.production")
else:
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.dev")

application = get_wsgi_application()
