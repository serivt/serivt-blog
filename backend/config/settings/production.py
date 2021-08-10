from .base import *  # NOQA
from .base import env

DEBUG = env.bool("DJANGO_DEBUG", default=False)

SECRET_KEY = env.str("DJANGO_SECRET_KEY")

ALLOWED_HOSTS = env.list("DJANGO_ALLOWED_HOST")

# Database

DATABASES = {"default": env.db("DJANGO_DATABASE_URL")}

DATABASES["default"]["ATOMIC_REQUESTS"] = env.bool(
    "DJANGO_ATOMIC_REQUESTS", default=False
)

DATABASES["default"]["CONN_MAX_AGE"] = env.int(
    "DJANGO_DATABASE_CONN_MAX_AGE", default=0
)

# Security

SECURE_PROXY_SSL_HEADER = ("DJANGO_HTTP_X_FORWARDED_PROTO", "https")

SECURE_SSL_REDIRECT = env.bool("DJANGO_SECURE_SSL_REDIRECT", default=True)

SESSION_COOKIE_SECURE = True

CSRF_COOKIE_SECURE = True

SECURE_HSTS_SECONDS = 60

SECURE_HSTS_INCLUDE_SUBDOMAINS = env.bool(
    "DJANGO_SECURE_HSTS_INCLUDE_SUBDOMAINS", default=True
)

SECURE_HSTS_PRELOAD = env.bool("DJANGO_SECURE_HSTS_PRELOAD", default=True)

SECURE_CONTENT_TYPE_NOSNIFF = env.bool(
    "DJANGO_SECURE_CONTENT_TYPE_NOSNIFF", default=True
)
