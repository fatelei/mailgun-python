#-*-coding: utf8-*-

"""
mailgun routers api
"""

from .client import MailgunClient


class APIRoutes(MailgunClient):

    """The routes api
    """

    def __init__(self, api_url=None, api_domain=None, api_key=None):
        """Init the class
        """
        super(APIRoutes, self).__init__(
            api_url=api_url, api_domain=api_domain, api_key=api_key)

    def get_routes(self, limit=100, skip=0):
        """Fetches the list of routes

        Args:
            limit: The maximum number of records to return
            skip: The number of records to skip
        """
        parameters = {"limit": limit,
                      "skip": skip}

        return self.get("routes", **parameters)

    def get_route(self, route_id):
        """Returns a single route object based on its ID

        Args:
            route_id: The id of the route
        """
        return self.get("routes/" + route_id)

    def create_route(self, priority, description, expression, action):
        """Creates a new route

        Args:
            priority: Integer: smaller number indicates higher priority. Higher priority routes are handled first. Defaults to 0
            description: An arbitrary string
            expression: A filter expression like match_recipient('.*@gmail.com')
            action: A route action
        """
        parameters = {"priority": priority,
                      "description": description,
                      "expression": expression,
                      "action": action}
        return self.post("routes", **parameters)

    def update_route(self, route_id, **kwargs):
        """Updates a given route by ID

        Args:
            route_id: The id of the route
            kwargs: 
                priority: Integer: smaller number indicates higher priority. Higher priority routes are handled first. Defaults to 0
                description: An arbitrary string
                expression: A filter expression like match_recipient('.*@gmail.com')
                action: A route action
        """
        return self.put("routes/" + route_id, **kwargs)

    def remove_route(self, route_id):
        """Deletes a route based on the id

        Args:
            route_id: The id of the route
        """
        return self.delete("routes/" + route_id)
