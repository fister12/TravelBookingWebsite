# PythonAnywhere Deployment Guide for Django Travel Booking App

## Prerequisites
1. PythonAnywhere account (free or paid)
2. Your code uploaded to GitHub


## Step-by-Step Deployment

### 1. Set Up Your PythonAnywhere Environment

#### A. Open a Bash Console on PythonAnywhere
- Go to your PythonAnywhere dashboard
- Click on "Consoles" → "Bash"

#### B. Clone Your Repository
```bash
git clone https://github.com/yourusername/travel-booking-app.git
cd travel-booking-app
```

#### C. Create and Activate Virtual Environment
```bash
python3.10 -m venv travel_env
source travel_env/bin/activate
```

#### D. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Database Setup

#### A. Create MySQL Database
1. Go to PythonAnywhere Dashboard → Databases
2. Create a new MySQL database named: `yourusername$travel_booking`
3. Note down the database details (host, username, password)

#### B. Update Production Settings
Edit `travel_project/production_settings.py` and update:
```python
ALLOWED_HOSTS = ['yourusername.pythonanywhere.com']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'yourusername$travel_booking',
        'USER': 'yourusername',
        'PASSWORD': 'your_actual_mysql_password',
        'HOST': 'yourusername.mysql.pythonanywhere-services.com',
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
        },
    }
}

STATIC_ROOT = '/home/yourusername/travel_project/static'
MEDIA_ROOT = '/home/yourusername/travel_project/media'
```

#### C. Run Migrations
```bash
cd travel_project
python manage.py migrate --settings=travel_project.production_settings
```

#### D. Create Superuser
```bash
python manage.py createsuperuser --settings=travel_project.production_settings
```

#### E. Create Sample Data (Optional)
```bash
python manage.py create_sample_data --settings=travel_project.production_settings
```

#### F. Collect Static Files
```bash
python manage.py collectstatic --settings=travel_project.production_settings
```

### 3. Web App Configuration

#### A. Create Web App
1. Go to PythonAnywhere Dashboard → Web
2. Click "Add a new web app"
3. Choose "Manual configuration"
4. Select Python 3.10

#### B. Configure WSGI File
1. In the Web tab, find the "Code" section
2. Click on the WSGI configuration file link
3. Replace the contents with:

```python
#!/usr/bin/env python

import os
import sys

# Add your project directory to sys.path
path = '/home/yourusername/travel_project'
if path not in sys.path:
    sys.path.insert(0, path)

# Set the Django settings module
os.environ['DJANGO_SETTINGS_MODULE'] = 'travel_project.production_settings'

# Import Django and setup
import django
django.setup()

# Import the WSGI application
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
```

#### C. Set Virtual Environment
1. In the Web tab, find "Virtualenv" section
2. Enter: `/home/yourusername/travel_env`

#### D. Configure Static Files
1. In the Web tab, find "Static files" section
2. Add:
   - URL: `/static/`
   - Directory: `/home/yourusername/travel_project/static`
3. Add (if using media files):
   - URL: `/media/`
   - Directory: `/home/yourusername/travel_project/media`

### 4. Final Steps

#### A. Reload Web App
Click the green "Reload" button in the Web tab

#### B. Test Your Application
Visit: `https://yourusername.pythonanywhere.com`

### 5. Common Issues and Solutions

#### Issue: ModuleNotFoundError
**Solution:** Make sure your virtual environment path is correct in the Web tab

#### Issue: Database Connection Error
**Solution:** Double-check your database credentials in production_settings.py

#### Issue: Static Files Not Loading
**Solution:** 
1. Run `python manage.py collectstatic` again
2. Check static files configuration in Web tab

#### Issue: DisallowedHost Error
**Solution:** Add your PythonAnywhere domain to `ALLOWED_HOSTS` in production_settings.py

### 6. Updating Your App

When you make changes to your code:

1. **Update code:**
```bash
cd /home/yourusername/travel_project
git pull origin main
```

2. **Update dependencies (if changed):**
```bash
source ../travel_env/bin/activate
pip install -r requirements.txt
```

3. **Run migrations (if models changed):**
```bash
python manage.py migrate --settings=travel_project.production_settings
```

4. **Collect static files (if static files changed):**
```bash
python manage.py collectstatic --settings=travel_project.production_settings
```

5. **Reload web app** from the Web tab

## Important Notes

### Free Account Limitations
- One web app
- Custom domains not available
- CPU seconds limit
- Database storage limit

### Paid Account Benefits
- Multiple web apps
- Custom domains
- More CPU seconds
- Larger database storage
- Always-on tasks

### Security Considerations
- Never commit sensitive data (passwords, secret keys) to Git
- Use environment variables for sensitive settings
- Keep DEBUG = False in production
- Regularly update dependencies

### Monitoring and Maintenance
- Check error logs in the Web tab
- Monitor CPU usage
- Regular database backups
- Keep Django and dependencies updated

## Troubleshooting Commands

```bash
# Check logs
tail -f /var/log/yourusername.pythonanywhere.com.error.log

# Test Django settings
python manage.py check --settings=travel_project.production_settings

# Test database connection
python manage.py dbshell --settings=travel_project.production_settings

# View installed packages
pip list

# Check Python path
python -c "import sys; print('\n'.join(sys.path))"
```

## Getting Help
- PythonAnywhere Forums: https://www.pythonanywhere.com/forums/
- PythonAnywhere Help: https://help.pythonanywhere.com/
- Django Documentation: https://docs.djangoproject.com/
