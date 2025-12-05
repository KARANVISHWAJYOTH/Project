# Classified Marketplace

A Django-based classifieds marketplace where users can buy and sell second-hand items with features like authentication, item posting, browsing, searching, filtering, and buyer-seller chat.

## Features

- ✅ User authentication (Signup/Login/Logout)
- ✅ Category-based browsing (Laptops, Phones, Cars, Furniture, etc.)
- ✅ Post listings with images, title, description, category, and price
- ✅ Search and filter listings (by title, category, price range)
- ✅ Listing detail pages with related items
- ✅ Buyer-seller chat functionality
- ✅ Search history tracking
- ✅ Beautiful, modern UI with responsive design
- ✅ Image upload and storage
- ✅ User can edit/delete their own listings

## Tech Stack

- **Backend**: Django 5.2.8
- **Database**: SQLite (default)
- **Image Processing**: Pillow
- **Filtering**: django-filter
- **Frontend**: HTML + CSS (no frameworks)

## Installation & Setup

### 1. Install Python Dependencies

```bash
pip install -r requirements.txt
```

### 2. Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 3. Create Default Categories

```bash
python manage.py create_categories
```

This will create the following categories:
- 💻 Laptops
- 📱 Phones
- 🚗 Cars
- 🪑 Furniture
- 📺 Electronics
- 👕 Clothing
- 📚 Books
- ⚽ Sports
- 🧸 Toys
- 🏡 Home & Garden
- 📦 Other

### 4. Create a Superuser (Optional - for admin access)

```bash
python manage.py createsuperuser
```

### 5. Run the Development Server

```bash
python manage.py runserver
```

The application will be available at `http://127.0.0.1:8000/`

## Project Structure

```
classifieds_marketplace/
├── accounts/          # User authentication app
│   ├── forms.py      # Signup and login forms
│   ├── views.py      # Authentication views
│   └── urls.py       # Account URLs
├── listings/         # Listings app
│   ├── models.py     # Category, Listing, SearchHistory models
│   ├── views.py      # Listing CRUD and search views
│   ├── forms.py      # Listing and search forms
│   ├── urls.py       # Listing URLs
│   └── management/
│       └── commands/
│           └── create_categories.py
├── chat/             # Chat app
│   ├── models.py     # Message model
│   ├── views.py      # Chat views
│   ├── forms.py      # Message form
│   └── urls.py       # Chat URLs
├── templates/        # HTML templates
│   ├── base.html
│   ├── accounts/
│   ├── listings/
│   └── chat/
├── static/           # Static files
│   └── css/
│       └── style.css
├── media/            # Uploaded images (created automatically)
├── marketplace/      # Main project settings
│   ├── settings.py
│   └── urls.py
└── requirements.txt
```

## Usage Guide

### For Users

1. **Sign Up / Login**: Visit the homepage to create an account or login
2. **Browse Categories**: Click on any category icon to see all items in that category
3. **Search**: Use the search page to find items by title, category, or price range
4. **Post Item**: Click "Post Item" to create a new listing with image, title, description, category, and price
5. **View Details**: Click on any listing to see full details
6. **Contact Seller**: Click "Contact Seller" on a listing to start a chat
7. **Manage Listings**: View and edit your own listings from "My Listings"

### For Developers

- **Admin Panel**: Access at `/admin/` (requires superuser)
- **Models**: All models are registered in admin for easy management
- **Media Files**: Uploaded images are stored in `media/listings/`
- **Static Files**: CSS files are in `static/css/`

## Key URLs

- `/` - Welcome/Login page
- `/home/` - Homepage with categories
- `/category/<slug>/` - Category listings
- `/listing/<id>/` - Listing detail
- `/create/` - Create new listing
- `/search/` - Search listings
- `/my-listings/` - User's listings
- `/chat/` - Chat conversations
- `/admin/` - Django admin panel

## Database Models

### Category
- name, icon, slug, created_at

### Listing
- title, description, category, price, image, owner, created_at, updated_at, is_sold

### Message
- sender, receiver, listing, content, sent_at, is_read

### SearchHistory
- user, query, category, min_price, max_price, results_count, searched_at

## Notes

- Images are stored in `media/listings/` directory
- All search queries are logged in the database
- Users can only edit/delete their own listings
- Chat messages are linked to listings when started from a listing page
- The application uses Django's built-in authentication system

## Troubleshooting

1. **Images not displaying**: Make sure `MEDIA_ROOT` and `MEDIA_URL` are correctly configured in settings.py
2. **Static files not loading**: Run `python manage.py collectstatic` (for production)
3. **Categories missing**: Run `python manage.py create_categories`
4. **Database errors**: Run `python manage.py migrate` to apply migrations

## License

This project is open source and available for educational purposes.





