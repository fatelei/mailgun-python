#-*-coding: utf8-*-

"""
mailgun client
"""

import requests

from mailgun import exceptions


class MailGunClient(object):

    def __init__(self, api_url=None, api_domain=None, api_key=None):
        """
        :param api_url: mailgun api base url
        :param api_domain: mailgun api domain
        :param api_key: mailgun api key
        """
        self.api_url = api_url
        self.api_domain = api_domain
        self.api_key = api_key

    def execute(self, method, url, **parameters):
        """
        execute mailgun api request
        :param method: http method
        :param url: full api url
        :param parameters: api request parameters
        """
        try:
            func = getattr(requests, method)
            resp = func(url, auth=("api", self.api_key), data=parameters)
            return self.response(resp)
        except Exception as e:
            raise e

    def response(self, resp):
        """
        get json from response
        """
        status_code = resp.status_code

        if status_code == 200:
            return resp.text
        else:
            if status_code == 400:
                raise exceptions.BadRequestException(msg=resp.text)
            elif status_code == 401:
                raise exceptions.UnauthorizeException(msg=resp.text)
            elif status_code == 402:
                raise exceptions.RequestFailedException(msg=resp.text)
            elif status_code == 404:
                raise exceptions.NotFoundException(msg=resp.text)
            else:
                raise exceptions.ServerErrorsException(
                    code=status_code, msg=resp.text)

    def generate_api_url(self, api):
        """
        generate api
        """
        if self.api_domain is not None:
            url = "{0}/{1}/{2}".format(self.api_url, self.api_domain, api)
        else:
            url = "{0}/{1}".format(self.api_url, api)
        return url

    def get(self, api, **parameters):
        """
        :param api: api type
        :param parameters: api parameters
        """
        url = self.generate_api_url(api)
        return self.execute("get", url, **parameters)

    def post(self, api, **parameters):
        """
        :param api: api type
        :param parameters: api parameters
        """
        url = self.generate_api_url(api)
        return self.execute("post", url, **parameters)

    def delete(self, api, **parameters):
        """
        :param api: api type
        :param parameters: api parameters
        """
        url = self.generate_api_url(api)
        return self.execute("delete", url, **parameters)

    def put(self, api, **parameters):
        """
        :param api: api type
        :param parameters: api parameters
        """
        url = self.generate_api_url(api)
        return self.execute("put", url, **parameters)
