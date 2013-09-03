#!/usr/bin/python
#-*-coding: utf8-*-

from mailgun.data.stats_data import StatsData
from mailgun.stats import Stats

if __name__ == "__main__":
    sd = StatsData()
    sd.add_paging_param()
    sd.add_events("sent")
    sd.add_start_date("2013-08-31")

    data = sd.to_request_data("GET")
    print data

    kwargs = {"data": data}
    s = Stats("domain", "api-key")
    print s.get_stats(**kwargs)