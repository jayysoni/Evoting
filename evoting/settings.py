from pathlib import Path
import os

# Base directory of the project (where manage.py is located)
BASE_DIR = Path(__file__).resolve().parent.parent

# Security settings
SECRET_KEY = 'django-insecure-q8sftyt^bdzdn)sg@9s--unq(-2s(d9-9y3ot13ebc#hpm7ng3'  # Secret key for security

DEBUG = True  # Set to False in production for security

ALLOWED_HOSTS = ['127.0.0.1', 'localhost']  # Allowed hosts (keep empty for development)

# Installed applications (Django's built-in + our custom apps)
INSTALLED_APPS = [
    'django.contrib.admin',  # Admin panel
    'django.contrib.auth',  # Authentication system
    'django.contrib.contenttypes',  # Content framework
    'django.contrib.sessions',  # Session management
    'django.contrib.messages',  # Flash messages
    'django.contrib.staticfiles',  # Static file handling
    'home',


]

# Middleware (used for request/response processing)
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',  # Basic security
    'django.contrib.sessions.middleware.SessionMiddleware',  # Handles sessions
    'django.middleware.common.CommonMiddleware',  # Basic middleware (like adding headers)
    'django.middleware.csrf.CsrfViewMiddleware',  # Protects against CSRF attacks
    'django.contrib.auth.middleware.AuthenticationMiddleware',  # Manages user authentication
    'django.contrib.messages.middleware.MessageMiddleware',  # Enables message framework
    'django.middleware.clickjacking.XFrameOptionsMiddleware',  # Prevents clickjacking
]

ROOT_URLCONF = 'evoting.urls'  # Main URL configuration

# Template settings (HTML files)
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',  # Django template engine
        'DIRS': [os.path.join(BASE_DIR, "templates")],  # ✅ Path where templates are stored
        'APP_DIRS': True,  # Look for templates inside apps
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',  # Debugging
                'django.template.context_processors.request',  # Gives access to request in templates
                'django.contrib.auth.context_processors.auth',  # User authentication in templates
                'django.contrib.messages.context_processors.messages',  # Enables messages in templates
            ],
        },
    },
]

WSGI_APPLICATION = 'evoting.wsgi.application'  # WSGI application entry point

# Database configuration (SQLite by default, change for production)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',  # Database engine
        'NAME': BASE_DIR / 'db.sqlite3',  # Database file location
    }
}

# Password validation rules (used during user registration)
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},  # Prevents easy-to-guess passwords
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},  # Enforces minimum password length
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},  # Prevents commonly used passwords
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},  # Prevents fully numeric passwords
]
# Authentication settings (default Django authentication backend)
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',  # Default authentication
]

# Login & logout redirect settings
LOGIN_URL = "accounts/login/"  # Redirect to login page if not logged in
LOGIN_REDIRECT_URL = "/vote/"  # Redirect voters to voting page after login
LOGOUT_REDIRECT_URL = "/login/"  # Redirect after logout

# Language and timezone settings
LANGUAGE_CODE = 'en-us'  # Language setting
TIME_ZONE = 'UTC'  # Time zone setting
USE_I18N = True  # Enable internationalization
USE_TZ = True  # Enable timezone support

# Static file settings (CSS, JS, images)
STATIC_URL = "static/"  # URL prefix for static files
STATICFILES_DIRS = [
    BASE_DIR / "static",  # ✅ Path where static files are stored
]

# Default auto field for models
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"