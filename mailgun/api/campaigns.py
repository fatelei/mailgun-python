#-*-coding: utf8-*-

"""
mailgun campaigns api
"""

from .client import MailgunClient


class APICampaigns(MailgunClient):

    """The campains api
    """

    def __init__(self, api_url=None, api_domain=None, api_key=None):
        """Init the class
        """
        super(APICampaigns, self).__init__(
            api_url=api_url, api_domain=api_domain, api_key=api_key)

    def get_campaigns(self, limit=100, skip=0):
        """Returns the list of the campaigns created for a given domain

        Args:
            limit: The maximum number of records to return
            skip: The number of records to skip
        """

        parameters = {"limit": limit,
                      "skip": skip}
        return self.get("campaigns", **parameters)

    def get_campaign(self, campaign_id):
        """Returns a single campaign for a given domain

        Args:
            campaign_id: The id of campaign
        """
        return self.get("campaigns/" + campaign_id)

    def create_campaign(self, name):
        """Creates a new campaign under a given domain

        Args:
            name: The name of the campaign
        """
        parameters = {"name": name}
        return self.post("campaigns", **parameters)

    def update_campaign(self, campaign_id, name=None, new_id=None):
        """Updates existing campaign with a new name and/or new id

        Args:
            campaign_id: The old id of the campaign
            name: The new name of the campaign (optional)
            new_id: The new id of the campaign (optional)
        """
        parameters = {}
        if name is not None:
            parameters["name"] = name
        if new_id is not None:
            parameters["id"] = new_id

        return self.put("campaigns/" + campaign_id, **parameters)

    def remove_campaign(self, campaign_id):
        """Deletes the given campaign with all its data

        Args:
            campaign_id: The id of the campaign
        """
        return self.delete("campaigns/" + campaign_id)
