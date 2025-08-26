from .settings import *

# Simple production settings for PythonAnywhere with SQLite

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = False  # Uncomment once everything is working

# Update with your PythonAnywhere username
ALLOWED_HOSTS = ['yourusername.pythonanywhere.com', 'localhost', '127.0.0.1']

# Keep SQLite database (no MySQL setup required)
# The database will be created automatically
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Static files configuration
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'static'

# Media files (for future use)
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Basic security settings
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True

# Login/logout redirects
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'
