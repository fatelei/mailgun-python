#-*-coding: utf8-*-

"""
mailgun complaints api
"""

from .client import MailgunClient


class APIComplaints(MailgunClient):

    """The complaints api
    """

    def __init__(self, api_url=None, api_domain=None, api_key=None):
        """Init the class
        """
        super(APIComplaints, self).__init__(
            api_url=api_url, api_domain=api_domain, api_key=api_key)

    def get_complaints(self, limit=100, skip=0):
        """Fetches the list of complaints

        Args:
            limit: The maximum number of records to return
            skip: The number of records to skip
        """
        parameters = {"limit": limit,
                      "skip": skip}
        return self.get("complaints", **parameters)

    def get_complaint(self, address):
        """Fetches a single spam complaint by a given email address

        Args:
            address: The email address
        """
        return self.get("complaints/" + address)

    def add_to_complaints(self, address):
        """Adds an address to the complaints table

        Args:
            address: The email address
        """
        parameters = {"address": address}
        return self.post("complaints", **parameters)

    def remove_from_complaints(self, address):
        """Removes a given spam complaint

        Args:
            address: The email address
        """
        return self.delete("complaints/" + address)
