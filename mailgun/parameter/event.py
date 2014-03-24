#-*-coding: utf8-*-

"""
event data for api events
"""

class Event(object):

    def __init__(self):
        self.data = {"pretty": "yes"}

    def add_begin(self, begin):
        """
        add begin datetime, rfc2822 format
        :param begin: begin datetime
        """
        self.data["begin"] = begin

    def add_end(self, end):
        """
        add end datetime, rfc2822 format
        :param end: end datetime
        """
        self.data["end"] = end

    def add_limit_and_skip(self, limit=100, skip=0):
        """
        add limit and skip
        :param limit: maximum number of records to return
        :param skip: number of records to skip
        """
        self.data["skip"] = skip
        self.date["limit"] = limit

    def add_filter_option(self, field, expr):
        """
        add filter option
        :param field: filter option
        :param expr: filter expression
        """
        self.data[field] = expr

    def generate(self):
        """
        generate data
        """
        return self.data
