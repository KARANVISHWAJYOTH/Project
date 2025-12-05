import logging
from typing import List, Dict

import requests
from django.utils.text import slugify


logger = logging.getLogger(__name__)

DUMMYJSON_SEARCH_API = "https://dummyjson.com/products/search"
DUMMYJSON_ALL_API = "https://dummyjson.com/products"


def _transform_product(product: Dict, fallback_keyword: str) -> Dict:
    rating = product.get("rating", {})
    raw_price = product.get("price", 0) or 0
    try:
        price_value = float(raw_price)
    except (TypeError, ValueError):
        price_value = 0
    price_inr = round(price_value * 83, 2)
    price_display = f"₹{price_inr:,.2f}".rstrip('0').rstrip('.')
    return {
        "title": product.get("title"),
        "description": product.get("description"),
        "price": price_inr,
        "price_display": price_display,
        "image": product.get("thumbnail")
                 or product.get("images", [None])[0]
                 or f"https://source.unsplash.com/600x400/?{slugify(fallback_keyword)}",
        "category": product.get("category", "Marketplace"),
        "rating": rating if isinstance(rating, (int, float)) else product.get("rating"),
        "reviews": product.get("stock"),
    }


def fetch_external_products(keyword: str, limit: int = 4) -> List[Dict]:
    """
    Fetch fallback products tailored to the search query using DummyJSON API.
    """
    query = keyword or "marketplace"
    products: List[Dict] = []

    try:
        search_resp = requests.get(
            DUMMYJSON_SEARCH_API,
            params={"q": query, "limit": limit * 2},
            timeout=5,
        )
        search_resp.raise_for_status()
        data = search_resp.json()
        products = data.get("products", [])
    except requests.RequestException as exc:
        logger.warning("Search product fetch failed: %s", exc)

    if not products:
        try:
            all_resp = requests.get(
                DUMMYJSON_ALL_API,
                params={"limit": limit * 2},
                timeout=5,
            )
            all_resp.raise_for_status()
            products = all_resp.json().get("products", [])
        except requests.RequestException as exc:
            logger.warning("Fallback product fetch failed: %s", exc)
            return []

    trimmed = products[:limit]
    return [_transform_product(prod, query) for prod in trimmed]

