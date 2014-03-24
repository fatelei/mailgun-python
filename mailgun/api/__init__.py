#-*-coding: utf8-*-

"""
mailgun api

usage:
    
    >>> from mailgun.api import Messages
    >>> msg = Messages(api_url=api_url, api_domain=api_domain, api_key=api_key)
    >>> msg.send_message()
"""

from .bounces import Bounces
from .campaigns import Campaigns
from .complaints import Complaints
from .domains import Domains
from .events import Events
from .messages import Messages
from .stats import Stats
from .unsubscribes import Unsubscribes
from .validations import EmailValidations