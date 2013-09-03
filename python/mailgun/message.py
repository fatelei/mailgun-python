#!/usr/bin/python
#-*-coding: utf8-*-

"""
mailgun module: sending message
"""

from mailgun import Mailgun


class Message(Mailgun):

    def __init__(self, domain, api_key):
        super(Message, self).__init__(domain, api_key)

    def send_messages(self, *args, **kwargs):
        """
        sending messages
        """
        return self.post("messages", *args, **kwargs)
