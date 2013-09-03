#!/usr/bin/python
#-*-coding: utf8-*-

from base import Base


class BouncesData(Base):

    def __init__(self):
        self.address = None
        self.skip = 0
        self.limit = 100

    def add_address(self, address):
        """
        add address to bounces table
        """
        if address:
            self.validate_email(address)
            self.address = address

    def to_request_data(self, method):
        """
        convert to request json data
        """
        if method == "GET":
            data = {"skip": self.skip, "limit": self.limit}
        elif method == "POST":
            if self.address:
                data = {"address": self.address}
            else:
                raise Exception(u"the address of email is not valid")
        else:
            raise Exception(u"unknown http method")
        return data
