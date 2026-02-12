import os
from pathlib import Path
from dotenv import load_dotenv
from django.contrib.auth import get_user_model
BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR / ".env")

# SECURITY
SECRET_KEY = os.getenv("SECRET_KEY", "unsafe-secret-key")
DEBUG = os.getenv("DEBUG", "False") == "True"

ALLOWED_HOSTS = os.getenv(
    "ALLOWED_HOSTS",
    "127.0.0.1,localhost,chef-jq4v.onrender.com"
).split(",")

CSRF_TRUSTED_ORIGINS = [
    "https://chef-jq4v.onrender.com",
]

# Render proxy fix
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
USE_X_FORWARDED_HOST = True



INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'corsheaders',
    'recipes',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


ROOT_URLCONF = 'backend.urls'

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

WSGI_APPLICATION = 'backend.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

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

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

STATIC_URL = 'static/'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# CORS settings
CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOW_CREDENTIALS = True
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
]

# CSRF settings
CSRF_TRUSTED_ORIGINS = [
    'http://localhost:3000',
    'http://127.0.0.1:3000',
]

# REST Framework settings
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',
    ],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10
}

# Spoonacular API
SPOONACULAR_API_KEY = ''
SPOONACULAR_BASE_URL = 'https://api.spoonacular.com'
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# ---------- CREATE ADMIN AFTER DJANGO READY ----------
if os.environ.get("RENDER"):
    try:
        from django.contrib.auth import get_user_model
        User = get_user_model()

        username = os.environ.get("DJANGO_ADMIN_USERNAME", "admin")
        password = os.environ.get("DJANGO_ADMIN_PASSWORD", "admin123")
        email = os.environ.get("DJANGO_ADMIN_EMAIL", "admin@example.com")

        if not User.objects.filter(username=username).exists():
            User.objects.create_superuser(username, email, password)
            print("✅ Admin created on startup")
        else:
            print("ℹ️ Admin already exists")

    except Exception as e:
        print("Admin creation error:", e)
