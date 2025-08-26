# PythonAnywhere Deployment Checklist

## Pre-Deployment
- [ ] Create PythonAnywhere account
- [ ] Upload code to GitHub repository
- [ ] Update `production_settings.py` with your details
- [ ] Add `.gitignore` file

## On PythonAnywhere

### 1. Console Setup
- [ ] Open Bash console
- [ ] Clone repository: `git clone https://github.com/yourusername/repo-name.git`
- [ ] Create virtual environment: `python3.10 -m venv travel_env`
- [ ] Activate virtual environment: `source travel_env/bin/activate`
- [ ] Install dependencies: `pip install -r requirements.txt`

### 2. Database Setup
- [ ] Create MySQL database on PythonAnywhere dashboard
- [ ] Update database settings in `production_settings.py`
- [ ] Run migrations: `python manage.py migrate --settings=travel_project.production_settings`
- [ ] Create superuser: `python manage.py createsuperuser --settings=travel_project.production_settings`
- [ ] Create sample data: `python manage.py create_sample_data --settings=travel_project.production_settings`
- [ ] Collect static files: `python manage.py collectstatic --settings=travel_project.production_settings`

### 3. Web App Configuration
- [ ] Create new web app (Manual configuration, Python 3.10)
- [ ] Update WSGI configuration file
- [ ] Set virtual environment path: `/home/yourusername/travel_env`
- [ ] Add static files mapping: `/static/` → `/home/yourusername/travel_project/static`
- [ ] Add media files mapping: `/media/` → `/home/yourusername/travel_project/media`

### 4. Final Steps
- [ ] Reload web app
- [ ] Test website: `https://yourusername.pythonanywhere.com`
- [ ] Test admin panel: `https://yourusername.pythonanywhere.com/admin`
- [ ] Test user registration and booking flow

## Customization Required

### Files to Update:
1. **`production_settings.py`**
   - Replace `yourusername` with your actual PythonAnywhere username
   - Update MySQL password with your actual password
   - Update ALLOWED_HOSTS with your domain

2. **`wsgi.py`**
   - Replace `yourusername` with your actual username

3. **WSGI Configuration File on PythonAnywhere**
   - Update the path to your project directory

### Common Replacements:
- `yourusername` → Your actual PythonAnywhere username
- `your_mysql_password` → Your actual MySQL database password
- `repo-name` → Your actual GitHub repository name

## Testing Checklist
- [ ] Home page loads correctly
- [ ] User can register
- [ ] User can login/logout
- [ ] Travel search works
- [ ] Booking process works
- [ ] User can view bookings
- [ ] User can cancel bookings
- [ ] Admin panel is accessible
- [ ] Static files (CSS/JS) load correctly

## Troubleshooting
If something doesn't work:
1. Check error logs in PythonAnywhere Web tab
2. Verify all file paths are correct
3. Ensure virtual environment is properly configured
4. Check database connection settings
5. Verify static files configuration

## Updating Your App
When you make changes:
1. Push changes to GitHub
2. Pull changes on PythonAnywhere: `git pull origin main`
3. Activate virtual environment
4. Install new dependencies (if any)
5. Run migrations (if models changed)
6. Collect static files (if needed)
7. Reload web app
