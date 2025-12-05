# Setup Instructions for Classified Marketplace

## Quick Start Guide

Follow these steps to get the marketplace up and running:

### Step 1: Install Dependencies

Open your terminal/command prompt and navigate to the project directory, then run:

```bash
pip install -r requirements.txt
```

This will install:
- Django 5.2.8
- Pillow 11.0.0 (for image handling)
- django-filter 24.3 (for search/filtering)

### Step 2: Set Up Database

Run migrations to create the database tables:

```bash
python manage.py makemigrations
python manage.py migrate
```

### Step 3: Create Categories

Create the default categories (Laptops, Phones, Cars, Furniture, etc.):

```bash
python manage.py create_categories
```

### Step 4: Create Admin User (Optional)

Create a superuser account to access the Django admin panel:

```bash
python manage.py createsuperuser
```

Follow the prompts to set a username, email, and password.

### Step 5: Run the Server

Start the development server:

```bash
python manage.py runserver
```

### Step 6: Access the Application

Open your web browser and go to:
- **Main Application**: http://127.0.0.1:8000/
- **Admin Panel**: http://127.0.0.1:8000/admin/ (if you created a superuser)

## First Time Usage

1. **Sign Up**: Click on the "Sign Up" tab on the welcome page
2. **Create Account**: Enter username, email, and password
3. **Browse Categories**: After logging in, you'll see category icons on the homepage
4. **Post Your First Item**: Click "Post Item" in the navigation bar
5. **Search Items**: Use the search page to find items by keyword, category, or price

## Troubleshooting

### Issue: "No module named 'Pillow'"
**Solution**: Make sure you've installed all requirements:
```bash
pip install -r requirements.txt
```

### Issue: Images not displaying
**Solution**: 
1. Make sure the `media` folder exists in your project root
2. Check that `MEDIA_ROOT` and `MEDIA_URL` are set correctly in `settings.py`
3. Restart the development server

### Issue: Categories not showing
**Solution**: Run the category creation command:
```bash
python manage.py create_categories
```

### Issue: Database errors
**Solution**: Make sure migrations are up to date:
```bash
python manage.py makemigrations
python manage.py migrate
```

### Issue: Static files not loading
**Solution**: For development, Django should serve static files automatically. If not:
1. Make sure `STATICFILES_DIRS` is set in `settings.py`
2. Restart the development server

## Project Structure

```
classifieds_marketplace/
├── accounts/          # Authentication
├── listings/          # Listings and categories
├── chat/              # Messaging system
├── templates/         # HTML templates
├── static/            # CSS and static files
├── media/             # Uploaded images (created automatically)
└── marketplace/       # Project settings
```

## Features Overview

- ✅ User registration and login
- ✅ Category-based browsing
- ✅ Post items with images
- ✅ Search and filter listings
- ✅ Chat with sellers
- ✅ Edit/delete your own listings
- ✅ Search history tracking

## Next Steps

1. Create your account
2. Browse existing categories
3. Post your first item
4. Start chatting with other users!

Enjoy using the Classified Marketplace! 🎉



