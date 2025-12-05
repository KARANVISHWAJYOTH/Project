# Troubleshooting Guide

## Common Issues and Solutions

### Issue 1: "No module named 'django'"
**Solution**: Install dependencies
```bash
pip install -r requirements.txt
```

### Issue 2: "No migrations to apply" or Database errors
**Solution**: Create and apply migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### Issue 3: "Categories not showing"
**Solution**: Create categories
```bash
python manage.py create_categories
```

### Issue 4: Server won't start
**Check these:**
1. Make sure you're in the project directory
2. Check if port 8000 is already in use
3. Try a different port: `python manage.py runserver 8080`

### Issue 5: "TemplateDoesNotExist" error
**Solution**: Make sure templates folder exists and is in the correct location
- Templates should be in: `templates/accounts/`, `templates/listings/`, `templates/chat/`
- Base template should be: `templates/base.html`

### Issue 6: Static files (CSS) not loading
**Solution**: 
1. Make sure `static/css/style.css` exists
2. Check `STATICFILES_DIRS` in settings.py
3. Restart the server

### Issue 7: Images not displaying
**Solution**:
1. Make sure `media/` folder exists in project root
2. Check `MEDIA_ROOT` and `MEDIA_URL` in settings.py
3. Restart the server

### Issue 8: "ImportError" or "ModuleNotFoundError"
**Solution**: Make sure all apps are in `INSTALLED_APPS` in settings.py:
- 'listings'
- 'accounts'
- 'chat'
- 'django_filters'

### Issue 9: "NoReverseMatch" error
**Solution**: Check URL patterns match the view names

### Issue 10: Login/Signup not working
**Check**:
1. Make sure `accounts.urls` is included in main urls.py
2. Check that welcome view exists in accounts/views.py

## Step-by-Step Setup Verification

Run these commands in order:

```bash
# 1. Check Django installation
python -c "import django; print(django.get_version())"

# 2. Check project setup
python manage.py check

# 3. Verify migrations
python manage.py showmigrations

# 4. Create migrations if needed
python manage.py makemigrations

# 5. Apply migrations
python manage.py migrate

# 6. Create categories
python manage.py create_categories

# 7. Run test script
python test_setup.py

# 8. Start server
python manage.py runserver
```

## If Server Starts But Pages Don't Load

1. **Check the URL**: Make sure you're accessing `http://127.0.0.1:8000/`
2. **Check browser console**: Press F12 and look for errors
3. **Check server logs**: Look at the terminal where server is running
4. **Clear browser cache**: Try Ctrl+F5 to hard refresh

## Getting More Information

To see detailed error messages:
```bash
python manage.py runserver --verbosity 2
```

To check for configuration issues:
```bash
python manage.py check --deploy
```

## Still Having Issues?

1. Check the error message in the terminal
2. Check the error message in the browser (if any)
3. Verify all files are in the correct locations
4. Make sure you've run all setup commands
5. Try deleting `db.sqlite3` and running migrations again (this will delete all data)


