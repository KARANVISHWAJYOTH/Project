import logging
import os
from typing import List, Dict

import requests

logger = logging.getLogger(__name__)

UNSPLASH_SEARCH_URL = "https://api.unsplash.com/search/photos"


def search_images(query: str, limit: int = 6) -> List[Dict]:
    """
    Fetch visually relevant images from Unsplash for a given query.
    Requires UNSPLASH_ACCESS_KEY in environment.
    """
    api_key = os.getenv("UNSPLASH_ACCESS_KEY")
    if not api_key or not query:
        return []

    params = {
        "query": query,
        "per_page": limit,
        "orientation": "landscape",
        "content_filter": "high",
    }
    headers = {"Authorization": f"Client-ID {api_key}"}

    try:
        resp = requests.get(UNSPLASH_SEARCH_URL, params=params, headers=headers, timeout=5)
        resp.raise_for_status()
        data = resp.json().get("results", [])
    except requests.RequestException as exc:
        logger.warning("Image search failed: %s", exc)
        return []

    results = []
    for item in data:
        urls = item.get("urls", {}) or {}
        results.append(
            {
                "title": item.get("description") or item.get("alt_description") or query,
                "url": urls.get("regular") or urls.get("full"),
                "thumb": urls.get("thumb") or urls.get("small"),
                "photographer": (item.get("user") or {}).get("name"),
            }
        )
    return [r for r in results if r.get("url")]

