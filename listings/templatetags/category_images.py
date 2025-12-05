from django import template

register = template.Library()

# Category-specific image mappings using free image services
CATEGORY_IMAGES = {
    'laptops': [
        'https://images.unsplash.com/photo-1496181133206-80ce9b88a853?w=200&h=150&fit=crop',
        'https://images.unsplash.com/photo-1525547719571-a2d4ac8945e2?w=200&h=150&fit=crop',
        'https://images.unsplash.com/photo-1517336714731-489689fd1ca8?w=200&h=150&fit=crop',
    ],
    'phones': [
        'https://images.unsplash.com/photo-1511707171634-5f897ff02aa9?w=200&h=150&fit=crop',
        'https://images.unsplash.com/photo-1592899677977-9c10ca588bbd?w=200&h=150&fit=crop',
        'https://images.unsplash.com/photo-1580910051074-3eb694886f8b?w=200&h=150&fit=crop',
    ],
    'cars': [
        'https://images.unsplash.com/photo-1494976388531-d1058494cdd8?w=200&h=150&fit=crop',
        'https://images.unsplash.com/photo-1503376780353-7e6692767b70?w=200&h=150&fit=crop',
        'https://images.unsplash.com/photo-1542362567-b07e54358753?w=200&h=150&fit=crop',
    ],
    'furniture': [
        'https://images.unsplash.com/photo-1555041469-a586c61ea9bc?w=200&h=150&fit=crop',
        'https://images.unsplash.com/photo-1506439773649-6e0eb8cfb237?w=200&h=150&fit=crop',
        'https://images.unsplash.com/photo-1524758631624-e2822e304c36?w=200&h=150&fit=crop',
    ],
    'electronics': [
        'https://images.unsplash.com/photo-1518770660439-4636190af475?w=200&h=150&fit=crop',
        'https://images.unsplash.com/photo-1550009158-9ebf69173e03?w=200&h=150&fit=crop',
        'https://images.unsplash.com/photo-1498049794561-7780e7231661?w=200&h=150&fit=crop',
    ],
    'clothing': [
        'https://images.unsplash.com/photo-1489987707025-afc232f7ea0f?w=200&h=150&fit=crop',
        'https://images.unsplash.com/photo-1558171813-4c088753af8f?w=200&h=150&fit=crop',
        'https://images.unsplash.com/photo-1523381210434-271e8be1f52b?w=200&h=150&fit=crop',
    ],
    'books': [
        'https://images.unsplash.com/photo-1512820790803-83ca734da794?w=200&h=150&fit=crop',
        'https://images.unsplash.com/photo-1495446815901-a7297e633e8d?w=200&h=150&fit=crop',
        'https://images.unsplash.com/photo-1524995997946-a1c2e315a42f?w=200&h=150&fit=crop',
    ],
    'sports': [
        'https://images.unsplash.com/photo-1461896836934- voices-of-the-game?w=200&h=150&fit=crop',
        'https://images.unsplash.com/photo-1579952363873-27f3bade9f55?w=200&h=150&fit=crop',
        'https://images.unsplash.com/photo-1517649763962-0c623066013b?w=200&h=150&fit=crop',
    ],
    'toys': [
        'https://images.unsplash.com/photo-1558060370-d644479cb6f7?w=200&h=150&fit=crop',
        'https://images.unsplash.com/photo-1566576912321-d58ddd7a6088?w=200&h=150&fit=crop',
        'https://images.unsplash.com/photo-1596461404969-9ae70f2830c1?w=200&h=150&fit=crop',
    ],
    'home-garden': [
        'https://images.unsplash.com/photo-1416879595882-3373a0480b5b?w=200&h=150&fit=crop',
        'https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=200&h=150&fit=crop',
        'https://images.unsplash.com/photo-1585320806297-9794b3e4eeae?w=200&h=150&fit=crop',
    ],
    'other': [
        'https://images.unsplash.com/photo-1586023492125-27b2c045efd7?w=200&h=150&fit=crop',
        'https://images.unsplash.com/photo-1523275335684-37898b6baf30?w=200&h=150&fit=crop',
        'https://images.unsplash.com/photo-1505740420928-5e560c06d30e?w=200&h=150&fit=crop',
    ],
}

DEFAULT_IMAGES = [
    'https://images.unsplash.com/photo-1523275335684-37898b6baf30?w=200&h=150&fit=crop',
    'https://images.unsplash.com/photo-1505740420928-5e560c06d30e?w=200&h=150&fit=crop',
    'https://images.unsplash.com/photo-1586023492125-27b2c045efd7?w=200&h=150&fit=crop',
]


@register.simple_tag
def get_category_images(category_slug):
    """Return list of image URLs for a category"""
    return CATEGORY_IMAGES.get(category_slug, DEFAULT_IMAGES)


@register.simple_tag
def get_category_image(category_slug, index=0):
    """Return a single image URL for a category by index"""
    images = CATEGORY_IMAGES.get(category_slug, DEFAULT_IMAGES)
    return images[index % len(images)]
