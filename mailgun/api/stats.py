#-*-coding: utf8-*-

"""
mailgun stats api
"""

from .client import MailGunClient


class APIStats(MailGunClient):

    def __init__(self, api_url=None, api_domain=None, api_key=None):
        super(APIStats, self).__init__(
            api_url=api_url, api_domain=api_domain, api_key=api_key)

    def get_stats(self, event, start_date, limit=100, skip=0):
        """
        returns a list of event stat items
        :param event: name of the event
        :param start_date: the date to receive the stats starting from, format YYYY-MM-DD
        :param limit: maximum number of records to return
        :param skip: number of records to skip
        """
        parameters = {"event": event,
                      "start_date": start_date,
                      "limit": limit,
                      "skip": skip}
        return self.get("stats", **parameters)

    def remove_tag_counters(self, tag):
        """
        deletes all counters for particular tag and the tag itself
        :param tag: name of the tag
        """
        return self.delete("tags/" + tag)
