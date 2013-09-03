#!/usr/bin/python
#-*-coding: utf8-*-

"""
mailgun module: stats
"""

from mailgun import Mailgun


class Stats(Mailgun):

    def __init__(self, domain, api_key):
        super(Stats, self).__init__(domain, api_key)

    def get_stats(self, *args, **kwargs):
        """
        get stats for specific event
        """
        return self.get("stats", *args, **kwargs)

    def remove_from_tags(self, *args, **kwargs):
        """
        remove event from tags
        """
        return self.delete("tags/{0}".format(args[0]), *args, **kwargs)
