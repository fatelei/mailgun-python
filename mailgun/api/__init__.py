#-*-coding: utf8-*-

"""
mailgun api

usage:
    
    >>> from mailgun.api import Messages
    >>> msg = Messages(api_url=api_url, api_domain=api_domain, api_key=api_key)
    >>> msg.send_message()
"""

from .bounces import APIBounces
from .campaigns import APICampaigns
from .complaints import APIComplaints
from .domains import APIDomains
from .events import APIEvents
from .messages import APIMessages
from .stats import APIStats
from .unsubscribes import APIUnsubscribes
from .validations import APIEmailValidations
from .routes import APIRoutes
from .mailinglists import APIMailingLists
