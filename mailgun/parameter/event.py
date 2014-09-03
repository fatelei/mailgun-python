#-*-coding: utf8-*-

"""
Event data for api events
"""


class Event(object):

    """The meta of event

    Attributes:
        data: A dict contains the info of an event
    """

    def __init__(self):
        """Init the class
        """
        self.data = {"pretty": "yes"}

    def add_begin(self, begin):
        """Add begin datetime, rfc2822 format
        
        Args:
            begin: A begin datetime
        """
        self.data["begin"] = begin

    def add_end(self, end):
        """Add end datetime, rfc2822 format
        
        Args:
            end: An end datetime
        """
        self.data["end"] = end

    def add_limit_and_skip(self, limit=100, skip=0):
        """Add limit and skip
        
        Args:
            limit: The maximum number of records to return
            skip: The number of records to skip
        """
        self.data["skip"] = skip
        self.date["limit"] = limit

    def add_filter_option(self, field, expr):
        """Add filter option
        
        Args:
            field: A filter option
            expr: A filter expression
        """
        self.data[field] = expr

    def generate(self):
        """Generate data
        """
        return self.data
