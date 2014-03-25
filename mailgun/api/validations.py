#-*-coding: utf8-*-

"""
mailgun email validation api
"""

from .client import MailGunClient


class APIEmailValidations(MailGunClient):

    def __init__(self, api_url=None, api_domain=None, api_key=None):
        super(EmailValidations, self).__init__(
            api_url=api_url, api_domain=api_domain, api_key=api_key)

    def validate(self, address):
        """
        given an arbitrary address, validates address based off defined checks
        :param address: email address
        """
        parameters = {"address": address}
        return self.get("address/validate", **parameters)

    def parse(self, addresses, syntax_only=True):
        """
        parses a delimiter separated list of email addresses into two lists:
        parsed addresses and unparsable portions

        :param addresses: list of addresses
        """
        parameters = {}
        parameters["addresses"] = ",".join(addresses)
        parameters["syntax_only"] = syntax_only

        return self.get("address/parse", **parameters)
