# Deploy Django Classified Marketplace on Render

## Prerequisites
- GitHub account with your project pushed
- Render account (free at render.com)

---

## Step 1: Prepare Your Project

### 1.1 Install Production Dependencies
```bash
pip install gunicorn whitenoise dj-database-url psycopg2-binary
pip freeze > requirements.txt
```

### 1.2 Create `render.yaml` (Optional - for Blueprint deployment)
Create a `render.yaml` file in your project root:
```yaml
services:
  - type: web
    name: classified-marketplace
    env: python
    buildCommand: "./build.sh"
    startCommand: "gunicorn marketplace.wsgi:application"
    envVars:
      - key: PYTHON_VERSION
        value: "3.11.0"
      - key: SECRET_KEY
        generateValue: true
      - key: DEBUG
        value: "False"
```

### 1.3 Create `build.sh`
Create a `build.sh` file in your project root:
```bash
#!/usr/bin/env bash
set -o errexit

pip install -r requirements.txt
python manage.py collectstatic --no-input
python manage.py migrate
```

Make it executable (on Linux/Mac):
```bash
chmod +x build.sh
```

---

## Step 2: Update Django Settings

### 2.1 Update `marketplace/settings.py`

Add these imports at the top:
```python
import os
import dj_database_url
```

Update these settings:
```python
# Security
SECRET_KEY = os.environ.get('SECRET_KEY', 'your-local-dev-key')
DEBUG = os.environ.get('DEBUG', 'True') == 'True'

ALLOWED_HOSTS = ['localhost', '127.0.0.1', '.onrender.com']

# Database - Use PostgreSQL in production
DATABASES = {
    'default': dj_database_url.config(
        default='sqlite:///db.sqlite3',
        conn_max_age=600
    )
}

# Static files with WhiteNoise
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # Add this line
    # ... rest of middleware
]

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_DIRS = [BASE_DIR / 'static']
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Media files (for user uploads)
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
```

---

## Step 3: Deploy on Render

### 3.1 Create a New Web Service
1. Go to [render.com](https://render.com) and sign in
2. Click **"New +"** → **"Web Service"**
3. Connect your GitHub repository
4. Select your `classifieds_marketplace` repo

### 3.2 Configure the Service
Fill in these settings:

| Setting | Value |
|---------|-------|
| **Name** | `classified-marketplace` |
| **Region** | Choose nearest to you |
| **Branch** | `main` |
| **Runtime** | `Python 3` |
| **Build Command** | `./build.sh` |
| **Start Command** | `gunicorn marketplace.wsgi:application` |

### 3.3 Add Environment Variables
Click **"Advanced"** and add these environment variables:

| Key | Value |
|-----|-------|
| `SECRET_KEY` | Click "Generate" for a random key |
| `DEBUG` | `False` |
| `PYTHON_VERSION` | `3.11.0` |

### 3.4 Create PostgreSQL Database (Optional but Recommended)
1. Click **"New +"** → **"PostgreSQL"**
2. Name it `classified-marketplace-db`
3. Choose **Free** plan
4. Click **"Create Database"**
5. Copy the **Internal Database URL**
6. Go back to your Web Service → Environment Variables
7. Add: `DATABASE_URL` = (paste the Internal Database URL)

### 3.5 Deploy
1. Click **"Create Web Service"**
2. Wait for the build to complete (5-10 minutes)
3. Your app will be live at `https://classified-marketplace.onrender.com`

---

## Step 4: Post-Deployment Setup

### 4.1 Create Superuser
1. Go to your Web Service on Render
2. Click **"Shell"** tab
3. Run:
```bash
python manage.py createsuperuser
```

### 4.2 Create Categories
In the same shell:
```bash
python manage.py create_categories
```

---

## Step 5: Handle Media Files (User Uploads)

Render's free tier doesn't persist files. For production, use cloud storage:

### Option A: Cloudinary (Recommended - Free tier available)
1. Sign up at [cloudinary.com](https://cloudinary.com)
2. Install: `pip install django-cloudinary-storage`
3. Add to settings:
```python
INSTALLED_APPS = [
    # ...
    'cloudinary_storage',
    'cloudinary',
]

CLOUDINARY_STORAGE = {
    'CLOUD_NAME': os.environ.get('CLOUDINARY_CLOUD_NAME'),
    'API_KEY': os.environ.get('CLOUDINARY_API_KEY'),
    'API_SECRET': os.environ.get('CLOUDINARY_API_SECRET'),
}

DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
```

### Option B: AWS S3
Use `django-storages` with S3 bucket.

---

## Troubleshooting

### Build Fails
- Check `requirements.txt` has all dependencies
- Ensure `build.sh` has correct line endings (LF, not CRLF)

### Static Files Not Loading
- Run `python manage.py collectstatic` locally to test
- Check `STATIC_ROOT` and `STATICFILES_DIRS` are correct

### Database Errors
- Ensure `DATABASE_URL` environment variable is set
- Check PostgreSQL database is running

### 500 Error
- Set `DEBUG=True` temporarily to see error details
- Check Render logs for stack trace

---

## Quick Commands Reference

```bash
# Local development
python manage.py runserver

# Collect static files
python manage.py collectstatic --no-input

# Run migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser
```

---

## Free Tier Limitations

- Web service spins down after 15 minutes of inactivity
- First request after spin-down takes ~30 seconds
- 750 hours/month free
- PostgreSQL free tier: 1GB storage, expires after 90 days

---

## Your Deployment Checklist

- [ ] Install gunicorn, whitenoise, dj-database-url, psycopg2-binary
- [ ] Update requirements.txt
- [ ] Create build.sh
- [ ] Update settings.py for production
- [ ] Push changes to GitHub
- [ ] Create Render Web Service
- [ ] Add environment variables
- [ ] Create PostgreSQL database (optional)
- [ ] Deploy and test
- [ ] Create superuser and categories
