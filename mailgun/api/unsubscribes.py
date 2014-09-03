#-*-coding: utf8-*-

"""
mailgun unsubscribe api
"""

from .client import MailgunClient


class APIUnsubscribes(MailgunClient):

    """The unsubscribe api
    """

    def __init__(self, api_url=None, api_domain=None, api_key=None):
        """Init the class
        """
        super(APIUnsubscribes, self).__init__(
            api_url=api_url, api_domain=api_domain, api_key=api_key)

    def get_unsubscribes(self, limit=100, skip=0):
        """Fetches the list of unsubscribes

        Args:
            limit: The maximum number of records to return
            skip: The number of records to skip
        """
        parameters = {"limit": limit,
                      "skip": skip}
        return self.get("unsubscribes", **parameters)

    def get_unsubscribe(self, address):
        """Retreives a single unsubscribe record

        Args:
            address: The email address
        """
        return self.get("unsubscribes/" + address)

    def remove_from_unsubscribe(self, address):
        """Removes an address from the unsubscribes table

        Args:
            address: The email address
        """
        return self.delete("unsubscribes/" + address)

    def add_to_unsubscribe(self, address):
        """Adds address to unsubscribed table

        Args:
            address: The email address
        """
        parameters = {"address": address,
                      "tag": "*"}
        return self.post("unsubscribes", **parameters)
