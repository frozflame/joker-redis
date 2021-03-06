#!/usr/bin/env python3
# coding: utf-8

import random
from collections import OrderedDict

from joker.cast import represent
from redis import Redis


class RedisExtended(Redis):
    def set_many(self, kvpairs, **kwargs):
        """
        :param kvpairs: a series of 2-tuples
        :param kwargs:
        """
        pipe = self.pipeline()
        for name, value in kvpairs:
            pipe.set(name, value, **kwargs)
        pipe.execute()

    def get_many(self, names):
        pipe = self.pipeline()
        for name in names:
            pipe.get(name)
        values = pipe.execute()
        if not values:
            return [None for _ in names]
        return values

    def rekom_getsetnx(self, name, value):
        # https://groups.google.com/d/msg/redis-db/QM15DH3SI6I/euJpdYJHTrcJ
        tmp_name = '_rekom_getsetnx_{}'.format(random.randint(1, 2 ** 60))
        pipe = self.pipeline()
        pipe.get(name)
        pipe.set(tmp_name, value)
        pipe.renamenx(tmp_name, name)
        pipe.delete(tmp_name)
        results = pipe.execute()
        return results[0]

    def __repr__(self):
        pool = getattr(self, 'connection_pool')
        kwargs = getattr(pool, 'connection_kwargs', {})
        params = OrderedDict([
            ('host', kwargs.get('host')),
            ('port', kwargs.get('port')),
            ('db', kwargs.get('db')),
        ])
        return represent(self, params)
