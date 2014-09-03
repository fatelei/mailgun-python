#-*-coding: utf8-*-

"""
mailgun events api
"""

from .client import MailgunClient


class APIEvents(MailgunClient):

	"""The events api
	"""

    def __init__(self, api_url=None, api_domain=None, api_key=None):
    	"""Init the class
    	"""
        super(APIEvents, self).__init__(
            api_url=api_url, api_domain=api_domain, api_key=api_key)

    def get_events(self, **parameters):
        """Query mailgun track events        
        """
        return self.get("events", **parameters)
