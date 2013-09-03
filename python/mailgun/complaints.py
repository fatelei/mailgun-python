#!/usr/bin/python
#-*-coding: utf8-*-

"""
mailgun module: spam complaints
"""

from mailgun import Mailgun


class Complaints(Mailgun):

    def __init__(self, domain, api_key):
        super(Complaints, self).__init__(domain, api_key)

    def get_complaints(self, *args, **kwargs):
        """
        get complaints list
        """
        return self.get("complaints", *args, **kwargs)

    def add_to_complaints(self, *args, **kwargs):
        """
        add email to complaints
        """
        return self.post("complaints", *args, **kwargs)

    def remove_from_complaints(self, *args, **kwargs):
        """
        remove email from complaints
        """
        return self.delete("complaints/{0}".format(args[0]), *args, **kwargs)
