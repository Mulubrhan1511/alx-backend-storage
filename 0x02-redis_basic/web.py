#!/usr/bin/env python3
"""web module
"""
from functools import wraps
from typing import Callable
import redis
import requests


def get_page(url: str) -> str:
    """Get the HTML content of a URL.

    Args:
        url: The URL to fetch.

    Returns:
        The HTML content of the URL.
    """

    redis_client = redis.Redis()

    key = "count:{url}".format(url=url.replace("/", "%2F"))
    count = redis_client.get(key)
    if count is None:
        count = 0

    redis_client.set(key, count + 1, ex=10)

    cache_key = "page:{url}".format(url=url.replace("/", "%2F"))
    cached_page = redis_client.get(cache_key)
    if cached_page is not None:
        return cached_page.decode("utf-8")

    page = requests.get(url).content.decode("utf-8")
    redis_client.set(cache_key, page, ex=10)

    return page


if __name__ == "__main__":
    url = "http://slowwly.robertomurray.co.uk"
    page = get_page(url)
    print(page)
