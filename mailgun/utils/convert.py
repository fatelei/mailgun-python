#!/usr/bin/python
#-*-coding: utf8-*-

"""
format convert tools
"""

import time

from email.utils import formatdate


def date_format(date):
    """Convert date to mailgun format
    
	Args:
    	date: Python datetime format
    """
    rfc_date = formatdate(time.mktime(date.timetuple()))
    return rfc_date
