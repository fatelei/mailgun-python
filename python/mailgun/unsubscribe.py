#!/usr/bin/python
#-*-coding: utf8-*-

"""
mailgun module: unsubscribes
"""


from mailgun import Mailgun


class Unsubscribe(Mailgun):

    def __init__(self, domain, api_key):
        super(Unsubscribe, self).__init__(domain, api_key)

    def get_unsubscribes(self, *args, **kwargs):
        """
        get the unsubscribes
        """
        return self._client.get("unsubscribes", *args, **kwargs)

    def remove_from_unsubscribe(self, *args, **kwargs):
        """
        remove address from unsubscribes
        """
        return self._client.delete(
                "unsubscribes/{0}".format(args[0]), *args, **kwargs)

    def add_to_unsubscribe(self, *args, **kwargs):
        """
        add address to unsubscribes
        """
        return self._client.post("unsubscribes", *args, **kwargs)
