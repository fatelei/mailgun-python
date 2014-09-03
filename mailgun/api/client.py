#-*-coding: utf8-*-

"""
mailgun client
"""

import requests

from mailgun import exceptions


class MailgunClient(object):

    """The base class of mailgun api

    Attributes:
        api_url: The base url of mailgun's api
        api_domain: The domain of mailgun's api
        api_key: The key of mailgun's api
    """

    def __init__(self, api_url=None, api_domain=None, api_key=None):
        """Init the class
        """
        self.api_url = api_url
        self.api_domain = api_domain
        self.api_key = api_key

    def execute(self, method, url, **parameters):
        """Execute mailgun api request

        Args:
            method: The HTTP method
            url: The full api url
            parameters: The parameters of the api

        Returns:
            The response info

        Raise:
            BadRequestException: The error of the client request.
            UnauthorizeException: The error of the invalid client request.
            RequestFailedException: Fail to execute the request.
            NotFoundException: The url isn't existed.
            ServerErrorsException: The server has some errors occured.
        """
        try:
            func = getattr(requests, method)
            resp = func(url, auth=("api", self.api_key), data=parameters)
            return self.response(resp)
        except Exception as e:
            raise e

    def response(self, resp):
        """Get the json data

        Args:
            resp: The HTTP's response instance

        Raise:
            BadRequestException: The error of the client request.
            UnauthorizeException: The error of the invalid client request.
            RequestFailedException: Fail to execute the request.
            NotFoundException: The url isn't existed.
            ServerErrorsException: The server has some errors occured.
        """
        status_code = resp.status_code

        if status_code == 200:
            return resp.json()
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
        """Generate the url of api

        Args:
            api: The name of mailgun's api

        Returns:
            The url of mailgun's api
        """
        if self.api_domain is not None:
            url = "{0}/{1}/{2}".format(self.api_url, self.api_domain, api)
        else:
            url = "{0}/{1}".format(self.api_url, api)
        return url

    def get(self, api, **parameters):
        """Execute the GET method

        Args:
            api: The name of mailgun's api
            parameters: The parameters used to execute the request
        """
        url = self.generate_api_url(api)
        return self.execute("get", url, **parameters)

    def post(self, api, **parameters):
        """Execute the POST method

        Args:
            api: The name of mailgun's api
            parameters: The parameters used to execute the request
        """
        url = self.generate_api_url(api)
        return self.execute("post", url, **parameters)

    def delete(self, api, **parameters):
        """Execute the PUT method

        Args:
            api: The name of mailgun's api
            parameters: The parameters used to execute the request
        """
        url = self.generate_api_url(api)
        return self.execute("delete", url, **parameters)

    def put(self, api, **parameters):
        """Execute the PUT method

        Args:
            api: The name of mailgun's api
            parameters: The parameters used to execute the request
        """
        url = self.generate_api_url(api)
        return self.execute("put", url, **parameters)
