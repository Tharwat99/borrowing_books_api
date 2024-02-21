import os 
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = os.getenv("SECRET_KEY", "django-insecure-=(3^l5vzt#dsui&lk)g51jag*l8=m(+_d&#d-2qgvx6w0ea1_p")
DEBUG = True

if DEBUG:
    import socket  # only if you haven't already imported this
    hostname, _, ips = socket.gethostbyname_ex(socket.gethostname())
    INTERNAL_IPS = [ip[: ip.rfind(".")] + ".1" for ip in ips] + ["127.0.0.1", "10.0.2.2"]


DB_ENGINE = os.getenv("DB_ENGINE", "django.db.backends.sqlite3")
DB_NAME = os.getenv("DB_NAME", os.path.join(BASE_DIR, "db.sqlite3"))
DB_HOST = os.getenv("DB_HOST", None)
DB_USER = os.getenv("DB_USER", None)
DB_PASSWORD = os.getenv("DB_PASSWORD", None)
DB_PORT = os.getenv("DB_PORT", None)

DATABASES = {
    "default": {
        "ENGINE": DB_ENGINE,
        "NAME": DB_NAME,
        'HOST': DB_HOST, 
        'USER': DB_USER,
        'PASSWORD': DB_PASSWORD,
        'PORT': '3306',
    }
}