#!/usr/bin/python
#-*-coding: utf8-*-


from datetime import datetime
from base import Base


class StatsData(Base):

    def __init__(self):
        self.skip = 0
        self.limit = 100
        self.events = []
        self.start_date = None

    def add_events(self, event):
        """
        add event
        """
        if event:
            self.validate_data_type(event, str)
            self.events.append(event)

    def add_start_date(self, date):
        """
        add start date
        """
        if date:
            self.validate_date(date)
            self.start_date = date

    def to_request_data(self, method):
        """
        convert request parameters

        :params
            method:  HTTP method, GET, DELETE
        """
        data = {}
        if method == "GET":
            data["skip"] = self.skip
            data["limit"] = self.limit
            data["event"] = self.events

            if self.start_date:
                data["start_date"] = self.start_date
            else:
                data["start_date"] = datetime.strftime("%Y-%m-%d")
            return data
        elif method == "DELETE":
            return data
        else:
            raise Exception(u"not allowed http method")
