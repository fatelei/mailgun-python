#!/usr/bin/python
#-*-coding: utf8-*-

import re


class Base(object):

    def __init__(self):
        raise NotImplementedError

    def validate_data_type(self, value, _type):
        """
        validate data type
        """
        if not isinstance(value, _type):
            raise ValueError(u"{0} must be {1}".format(value, _type))

    def validate_email(self, email):
        """
        validate the email address
        """
        regex = re.compile(
            r"^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$")
        if not regex.match(email):
            raise ValueError(u"invalid email address")

    def validate_date(self, date):
        """
        validate the date format
        """
        regex = re.compile(r"^\d{4}-\d{2}-\d{2}$")
        if not regex.match(date):
            raise ValueError(u"invalid date format")

    def add_paging_param(self, skip=0, limit=100):
        """
        add paging parameters
        """
        try:
            self.validate_data_type(skip, int)
            self.skip = skip
            self.validate_data_type(limit, int)
            self.limit = limit
        except Exception as e:
            pass
