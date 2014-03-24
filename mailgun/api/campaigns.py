#-*-coding: utf8-*-

"""
mailgun campaigns api
"""

from .client import MailGunClient


class Campaigns(MailGunClient):

    def __init__(self, api_url=None, api_domain=None, api_key=None):
        super(Campaigns, self).__init__(
            api_url=api_url, api_domain=api_domain, api_key=api_key)

    def get_campaigns(self, limit=100, skip=0):
        """
        returns the list of the campaigns created for a given domain
        :param limit: maximum number of records to return
        :param skip: number of records to skip
        """

        parameters = {"limit": limit,
                      "skip": skip}
        return self.get("campaigns", **parameters)

    def get_campaign(self, campaign_id):
        """
        returns a single campaign for a given domain
        :param campaign_id: id of campaign
        """
        return self.get("campaigns/" + campaign_id)

    def create_campaign(self, name):
        """
        creates a new campaign under a given domain
        :param name: name of the campaign
        """
        parameters = {"name": name}
        return self.post("campaigns", **parameters)

    def update_campaign(self, campaign_id, name=None, new_id=None):
        """
        updates existing campaign with a new name and/or new id
        :param campaign_id: old id of the campaign
        :param name: new name of the campaign (optional)
        :param _id: new id of the campaign (optional)
        """
        parameters = {}
        if name is not None:
            parameters["name"] = name
        if new_id is not None:
            parameters["id"] = new_id

        return self.put("campaigns/" + campaign_id, **parameters)

    def remove_campaign(self, campaign_id):
        """
        deletes the given campaign with all its data
        :param campaign_id: id of the campaign
        """
        return self.delete("campaigns/" + campaign_id)
