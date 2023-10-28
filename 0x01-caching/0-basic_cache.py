#!/usr/bin/env python3
"""Basc Dictionary
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """inherits from BaseCaching and is a caching system
    """
    def put(self, key, item):
        """add item in the cache.
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """gets an item by key.
        """
        return self.cache_data.get(key, None)
