#!/usr/bin/python
#-*-coding: utf8-*-

from mailgun.data.bounces_data import BouncesData
from mailgun.bounces import Bounces

if __name__ == "__main__":
    bd = BouncesData()
    bd.add_paging_param()

    data = bd.to_request_data("GET")

    kwargs = {}
    if data:
        kwargs["data"] = data
    b = Bounces("domain", "api-key")
    print b.get_bounces(**kwargs)

    
    bd.add_address("for@bar.com")
    data = bd.to_request_data("POST")
    kwargs = {}
    if data:
        kwargs["data"] = data
    print b.add_to_bounces(**kwargs)

    print b.remove_from_bounces("foo@bar.com")
