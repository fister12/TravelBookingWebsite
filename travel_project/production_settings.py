import os
from .settings import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# Update this with your PythonAnywhere username
ALLOWED_HOSTS = ['AadityaKapruwan.mysql.pythonanywhere-services.com']

# Database for PythonAnywhere (MySQL)
# You'll need to update these with your actual database details from PythonAnywhere
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'yourusername$travel_booking',
        'USER': 'yourusername',
        'PASSWORD': 'your_mysql_password',
        'HOST': 'yourusername.mysql.pythonanywhere-services.com',
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
        },
    }
}

# Static files configuration for PythonAnywhere
STATIC_URL = '/static/'
STATIC_ROOT = '/home/yourusername/travel_project/static'

# Media files configuration
MEDIA_URL = '/media/'
MEDIA_ROOT = '/home/yourusername/travel_project/media'

# Security settings for production
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True

# Email configuration (optional - for password reset emails)
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_PORT = 587
# EMAIL_USE_TLS = True
# EMAIL_HOST_USER = 'your_email@gmail.com'
# EMAIL_HOST_PASSWORD = 'your_app_password'
