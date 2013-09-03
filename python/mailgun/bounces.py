#!/usr/bin/python
#-*-coding: utf8-*-

"""
mailgun module: bounces
"""

from mailgun import Mailgun


class Bounces(Mailgun):

    def __init__(self, domain, api_key):
        super(Bounces, self).__init__(domain, api_key)

    def get_bounces(self, *args, **kwargs):
        """
        get the list of bounces
        """
        return self.get("bounces", *args, **kwargs)

    def get_single_bounces(self, *args, **kwargs):
        """
        judge the given address whether it is bounced
        """
        return self.get("bounces/{0}".format(args[0]), *args, **kwargs)

    def add_to_bounces(self, *args, **kwargs):
        """
        add address to bounces
        """
        return self.post("bounces", *args, **kwargs)

    def remove_from_bounces(self, *args, **kwargs):
        """
        remove address from bounces
        """
        return self.delete("bounces/{0}".format(args[0]), *args, **kwargs)
