#-*-coding: utf8-*-

"""
mailgun events api
"""

from .client import MailGunClient


class APIEvents(MailGunClient):

    def __init__(self, api_url=None, api_domain=None, api_key=None):
        super(Events, self).__init__(
            api_url=api_url, api_domain=api_domain, api_key=api_key)

    def get_events(self, **parameters):
        """
        query mailgun track events
        """
        return self.get("events", **parameters)
