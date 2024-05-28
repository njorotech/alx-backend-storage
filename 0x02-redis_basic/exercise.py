#!/usr/bin/env python3
"""Writing strings to Redis"""

from typing import Union
import redis
import uuid


class Cache:
    """Cache class"""

    def __init__(self):
        """
        Store an instance of the Redice client as a private variable named
        _redis (using redis.Redis()) and flush the instance using flushdb
        """

        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        store method that takes a data argument and returns a string.
        The method should generate a random key (e.g. using uuid),
        store the input data in Redis using random key and return the key.
        """

        random_uuid = str(uuid.uuid4())
        self._redis.mset({random_uuid: data})
        return random_uuid
