#-*-coding: utf8-*-

"""
mailgun complaints api
"""

from .client import MailGunClient


class APIComplaints(MailGunClient):

    def __init__(self, api_url=None, api_domain=None, api_key=None):
        super(APIComplaints, self).__init__(
            api_url=api_url, api_domain=api_domain, api_key=api_key)

    def get_complaints(self, limit=100, skip=0):
        """
        fetches the list of complaints
        
        @param limit: maximum number of records to return
        @param skip: number of records to skip
        """
        parameters = {"limit": limit,
                      "skip": skip}
        return self.get("complaints", **parameters)

    def get_complaint(self, address):
        """
        fetches a single spam complaint by a given email address
        
        @param address: email address
        """
        return self.get("complaints/" + address)

    def add_to_complaints(self, address):
        """
        adds an address to the complaints table
        
        @param address: email address
        """
        parameters = {"address": address}
        return self.post("complaints", **parameters)

    def remove_from_complaints(self, address):
        """
        removes a given spam complaint
        
        @param address: email address
        """
        return self.delete("complaints/" + address)
