#-*-coding: utf8-*-

"""
mailgun messages api
"""

from .client import MailgunClient


class APIMessages(MailgunClient):

    """The messages api
    """

    def __init__(self, api_url=None, api_domain=None, api_key=None):
        """Init the class
        """
        super(APIMessages, self).__init__(
            api_url=api_url, api_domain=api_domain, api_key=api_key)

    def send_message(self, **parameters):
        """Send message

        Args:
            parameters: The request parameters
        """
        return self.post("messages", **parameters)

    def send_mime_message(self, **parameters):
        """Send mime message

        Args:
            parameters: The request parameters
        """
        return self.post("message.mime", **parameters)
