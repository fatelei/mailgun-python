#-*-coding: utf8-*-

"""
mailgun bounces api
"""

from .client import MailGunClient


class APIBounces(MailGunClient):

    def __init__(self, api_url=None, api_domain=None, api_key=None):
        super(APIBounces, self).__init__(
            api_url=api_url, api_domain=api_domain, api_key=api_key)

    def get_bounces(self, limit=100, skip=0):
        """
        fetches the list of bounces
        @param limit: maximum number of records to return
        @param skip: number of records to skip
        """
        parameters = {"limit": limit,
                      "skip": skip}
        return self.get("bounces", **parameters)

    def get_bounce(self, address):
        """
        fetches a single bounce event by a given email address
        @param address: email address
        """
        return self.get("bounces/" + address)

    def add_to_bounces(self, address):
        """
        adds a permanent bounce to the bounces table
        @param address: email address
        """
        parameters = {"address": address,
                      "code": 550}
        return self.post("bounces", **parameters)

    def remove_from_bounces(self, address):
        """
        “Clears” a given bounce event
        @param address: email address
        """
        return self.delete("bounces/" + address)
