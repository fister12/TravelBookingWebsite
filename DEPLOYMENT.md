# Deployment Checklist

## Before Deployment

### Security Settings
- [ ] Set `DEBUG = False` in production
- [ ] Update `ALLOWED_HOSTS` with your domain
- [ ] Generate a new `SECRET_KEY` for production
- [ ] Use environment variables for sensitive data

### Database
- [ ] Configure production database (PostgreSQL/MySQL)
- [ ] Run migrations on production database
- [ ] Create superuser on production

### Static Files
- [ ] Configure static files serving
- [ ] Run `python manage.py collectstatic`
- [ ] Configure media files handling

### Performance
- [ ] Enable caching
- [ ] Configure logging
- [ ] Set up monitoring

### Backup
- [ ] Set up database backups
- [ ] Set up media files backup

## Production Environment Variables

Create a `.env` file or set environment variables:

```
SECRET_KEY=your-secret-key-here
DEBUG=False
DATABASE_URL=postgres://user:password@host:port/dbname
ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com
```

## Additional Features to Consider

- [ ] Email notifications for bookings
- [ ] Payment integration
- [ ] PDF ticket generation
- [ ] Search filters by price range
- [ ] User reviews and ratings
- [ ] Advanced booking management
- [ ] API endpoints for mobile app
- [ ] Multi-language support
- [ ] Social authentication
- [ ] Booking history analytics
