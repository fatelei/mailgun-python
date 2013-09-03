#!/usr/bin/python
#-*-coding: utf8-*-

import requests
import logging


class Transport(object):

    """
    communication with mailgun
    """

    def __init__(self, domain, api_key):
        self.domain = domain
        self.auth = ("api", api_key)
        # api url format: address/<domain>/action
        self.api_url = "https://api.mailgun.net/v2/{0}/{1}"

    def __generate_url(self, action):
        """
        build api url
        """
        return self.api_url.format(self.domain, action)

    def process(self, action, method, *args, **kwargs):
        """
        visit mailgun api
        """
        url = self.__generate_url(action)

        logging.warning(url)
        try:
            func = getattr(requests, method)
            resp = func(url, auth=self.auth, **kwargs)
            info = resp.json()
            info["code"] = resp.status_code
            return info
        except Exception as e:
            logging.warning(e)
            raise e
