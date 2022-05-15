import environ

from verbifyapp.settings.base import *

env = environ.Env()

ALLOWED_HOSTS = env.list("ALLOWED_HOSTS")

DATABASES = {
    "default": env.db(),
}