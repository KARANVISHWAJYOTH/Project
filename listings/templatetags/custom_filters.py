from django import template
import random

register = template.Library()

@register.filter
def random_choice(images_list):
    """Return a random image URL from the list of images"""
    if images_list and len(images_list) > 0:
        # For the image search results, we need to extract the URL
        if isinstance(images_list[0], dict):
            # It's the result from image_search.py with url key
            image_urls = [img.get('url') for img in images_list if img.get('url')]
            if image_urls:
                return random.choice(image_urls)
        else:
            # It's a simple list of URLs
            return random.choice(images_list)
    return ''