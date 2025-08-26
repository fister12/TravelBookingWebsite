# Simple PythonAnywhere Deployment Checklist (SQLite)

## ✅ Super Simple Deployment - No Database Setup Required!

### Prerequisites
- [x] PythonAnywhere account (free works!)
- [x] Code pushed to GitHub

### On PythonAnywhere (Easy Steps)

#### 1. Get Your Code
- [ ] Open Bash Console on PythonAnywhere
- [ ] Run: `git clone https://github.com/fister12/TravelBookingWebsite.git`
- [ ] Run: `cd TravelBookingWebsite/travel_project`
- [ ] Run: `bash check_structure.sh` (to verify everything is in place)

#### 2. Set Up Environment
- [ ] Run: `python3.10 -m venv ../travel_env` (create it one level up)
- [ ] Run: `source ../travel_env/bin/activate`
- [ ] Run: `pip install Django`

#### 3. Set Up Your App (SQLite - Super Easy!)
- [ ] You should already be in the travel_project directory
- [ ] Run: `python manage.py migrate` (creates database automatically!)
- [ ] Run: `python manage.py createsuperuser`
- [ ] Run: `python manage.py create_sample_data`
- [ ] Run: `python manage.py collectstatic --noinput`

#### 4. Create Web App
- [ ] Go to PythonAnywhere Dashboard → Web
- [ ] Click "Add a new web app"
- [ ] Choose "Manual configuration"
- [ ] Select "Python 3.10"

#### 5. Configure Web App
- [ ] **Source code**: `/home/yourusername/TravelBookingWebsite/travel_project`
- [ ] **Working directory**: `/home/yourusername/TravelBookingWebsite/travel_project`
- [ ] **Virtualenv**: `/home/yourusername/travel_env`

#### 6. Update WSGI File
- [ ] Click on WSGI configuration file link
- [ ] Replace ALL content with:

```python
#!/usr/bin/env python
import os
import sys

path = '/home/yourusername/TravelBookingWebsite/travel_project'
if path not in sys.path:
    sys.path.insert(0, path)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'travel_project.settings')

import django
django.setup()

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
```

#### 7. Static Files
- [ ] Add Static Files mapping:
  - **URL**: `/static/`
  - **Directory**: `/home/yourusername/TravelBookingWebsite/travel_project/static`

#### 8. Update Settings
- [ ] Edit `/home/yourusername/TravelBookingWebsite/travel_project/travel_project/settings.py`
- [ ] Find the line with `ALLOWED_HOSTS = []`
- [ ] Change it to: `ALLOWED_HOSTS = ['yourusername.pythonanywhere.com']`

#### 9. Go Live!
- [ ] Click the green "Reload" button
- [ ] Visit: `https://yourusername.pythonanywhere.com`
- [ ] Test: Register, login, book travel!

## 🎯 Replace These Before Deployment:
- Replace `yourusername` with your actual PythonAnywhere username in:
  - WSGI file paths
  - Static files path
  - ALLOWED_HOSTS setting
  - Website URL

## 🚀 That's It!

### Your app will be live at:
- **Website**: `https://yourusername.pythonanywhere.com`
- **Admin**: `https://yourusername.pythonanywhere.com/admin`

### Why This Approach is Great:
- ✅ No database configuration needed
- ✅ SQLite database created automatically
- ✅ Works with free PythonAnywhere account
- ✅ Quick deployment (under 30 minutes)
- ✅ Easy to update and maintain

### If Something Goes Wrong:
1. Check the error log in Web tab
2. Make sure all paths have your correct username
3. Ensure virtual environment is activated
4. Verify static files are collected

### To Update Your App Later:
```bash
cd TravelBookingWebsite
git pull origin main
cd travel_project
python manage.py migrate
python manage.py collectstatic --noinput
```
Then reload your web app!

**Need help?** Check `SIMPLE_DEPLOYMENT.md` for detailed instructions.
