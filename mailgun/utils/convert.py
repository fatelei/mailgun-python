#!/usr/bin/python
#-*-coding: utf8-*-

"""
format convert tools
"""

import time

from email.utils import formatdate


def date_format(date):
    """
    convert date to mailgun format
    @param date: python datetime format
    """
    rfc_date = formatdate(time.mktime(date.timetuple()))
    return rfc_date
