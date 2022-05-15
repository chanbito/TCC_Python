import environ

from verbifyapp.settings.base import *

env = environ.Env()

SECRET_KEY = env.list("SECRET_KEY")

ALLOWED_HOSTS = env.list("ALLOWED_HOSTS")

DATABASES = {
    "default": env.db(),
}