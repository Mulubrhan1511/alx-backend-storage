#!/usr/bin/env python3
'''A module with tools for request caching and tracking.
'''
import requests
import redis
import functools

CACHE_EXPIRATION = 10

def get_page(url: str) -> str:
    cache = redis.Redis()
    count_key = f"count:{url}"
    content_key = f"content:{url}"

    # Check if the content is already cached
    cached_content = cache.get(content_key)
    if cached_content is not None:
        return cached_content.decode("utf-8")

    # Fetch the page content
    response = requests.get(url)
    content = response.text

    # Cache the content with an expiration time
    cache.setex(content_key, CACHE_EXPIRATION, content)

    # Track the count of URL accesses
    cache.incr(count_key)

    return content
