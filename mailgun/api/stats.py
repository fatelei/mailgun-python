#-*-coding: utf8-*-

"""
mailgun stats api
"""

from .client import MailgunClient


class APIStats(MailgunClient):

    """The stats api
    """

    def __init__(self, api_url=None, api_domain=None, api_key=None):
        """Init the class
        """
        super(APIStats, self).__init__(
            api_url=api_url, api_domain=api_domain, api_key=api_key)

    def get_stats(self, event, start_date, limit=100, skip=0):
        """Returns a list of event stat items

        Args:
            event: A name of the event
            start_date: The date to receive the stats starting from, format YYYY-MM-DD
            limit: The maximum number of records to return
            skip: The number of records to skip
        """
        parameters = {"event": event,
                      "start_date": start_date,
                      "limit": limit,
                      "skip": skip}
        return self.get("stats", **parameters)

    def remove_tag_counters(self, tag):
        """Deletes all counters for particular tag and the tag itself

        Args:
            tag: The name of the tag
        """
        return self.delete("tags/" + tag)
