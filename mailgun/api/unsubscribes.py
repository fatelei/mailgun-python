#-*-coding: utf8-*-

"""
mailgun unsubscribe api
"""

from .client import MailGunClient


class Unsubscribes(MailGunClient):

    def __init__(self, api_url=None, api_domain=None, api_key=None):
        super(Unsubscribes, self).__init__(
            api_url=api_url, api_domain=api_domain, api_key=api_key)

    def get_unsubscribes(self, limit=100, skip=0):
        """
        fetches the list of unsubscribes
        :param limit: maximum number of records to return
        :param skip: number of records to skip
        """
        parameters = {"limit": limit,
                      "skip": skip}
        return self.get("unsubscribes", **parameters)

    def get_unsubscribe(self, address):
        """
        retreives a single unsubscribe record
        :param address: email address
        """
        return self.get("unsubscribes/" + address)

    def remove_from_unsubscribe(self, address):
        """
        removes an address from the unsubscribes table
        :param address: email address
        """
        return self.delete("unsubscribes/" + address)

    def add_to_unsubscribe(self, address):
        """
        adds address to unsubscribed table
        :param address: email address
        """
        parameters = {"address": address,
                      "tag": "*"}
        return self.post("unsubscribes", **parameters)
