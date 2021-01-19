from .base import *

DEBUG = False

ALLOWED_HOSTS = [env("PRODUCTION_URL")]
SECRET_KEY = env("SECRET_KEY")