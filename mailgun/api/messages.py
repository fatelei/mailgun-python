#-*-coding: utf8-*-

"""
mailgun messages api
"""

from .client import MailGunClient


class APIMessages(MailGunClient):

    def __init__(self, api_url=None, api_domain=None, api_key=None):
        super(APIMessages, self).__init__(
            api_url=api_url, api_domain=api_domain, api_key=api_key)

    def send_message(self, **parameters):
        """
        send normal message
        :param parameters: request parameters
        """
        return self.post("messages", **parameters)

    def send_mime_message(self, **parameters):
        """
        send mime message
        :param parameters: request parameters
        """
        return self.post("message.mime", **parameters)
