#-*-coding: utf8-*-

"""
Mailgun bounces api
"""

from .client import MailgunClient


class APIBounces(MailgunClient):

    """The class of bounces api   
    """

    def __init__(self, api_url=None, api_domain=None, api_key=None):
        """Init the class
        """
        super(APIBounces, self).__init__(
            api_url=api_url, api_domain=api_domain, api_key=api_key)

    def get_bounces(self, limit=100, skip=0):
        """Fetches the list of bounces

        Args:
            limit: The maximum number of records to return
            skip: The number of records to skip

        Returns:
            A dict contains the info of bounces.
            For example:

            {
                "total_count": 1,
                "items": [
                    {
                        "created_at": "Fri, 21 Oct 2011 11:02:55 GMT",
                        "code": 550,
                        "address": "'baz@example.com",
                        "error": "Message was not accepted -- invalid mailbox.  Local mailbox 'baz@example.com is unavailable: user not found"
                    }
                ]
            }
        """
        parameters = {"limit": limit,
                      "skip": skip}
        data = self.get("bounces", **parameters)
        return data

    def get_bounce(self, address):
        """Fetches a single bounce event by a given email address

        Args:
            address: The email address

        Returns:
            A dict contains the info that whether the address is bounced.
            For example:

            {
                "message": "Address not found in bounces table"
            }
        """
        data = self.get("bounces/" + address)
        return data

    def add_to_bounces(self, address):
        """Add a permanent bounce to the bounces table

        Args:
            address: The email address

        Returns:
            A dict contains the info of the response
            For example:

            {
                "message": "Address has been added to the bounces table",
                "address": "bob@example.com"
            }
        """
        parameters = {"address": address,
                      "code": 550}
        data = self.post("bounces", **parameters)
        return data

    def remove_from_bounces(self, address):
        """Remove the email from the bounce events

        Args:
            address: The email address
        """
        return self.delete("bounces/" + address)
