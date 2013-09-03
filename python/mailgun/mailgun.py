#!/usr/bin/python
#-*-coding: utf8-*-

from transport import Transport


class Mailgun(object):

    def __init__(self, domain, api_key):
        self._client = Transport(domain, api_key)

    def get(self, action, *args, **kwargs):
        """
        HTTP GET method
        """
        return self._client.process(action, "get", *args, **kwargs)

    def post(self, action, *args, **kwargs):
        """
        HTTP POST method
        """
        return self._client.process(action, "post", *args, **kwargs)

    def delete(self, action, *args, **kwargs):
        """
        HTTP DELETE method
        """
        return self._client.process(action, "delete", *args, **kwargs)

    def put(self, action, *args, **kwargs):
        """
        HTTP PUT method
        """
        return self._client.process(action, "put", *args, **kwargs)
