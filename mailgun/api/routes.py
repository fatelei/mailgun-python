#-*-coding: utf8-*-

"""
mailgun routers api
"""

from .client import MailGunClient


class Routes(MailGunClient):

    def __init__(self, api_url=None, api_domain=None, api_key=None):
        super(Routers, self).__init__(
            api_url=api_url, api_domain=api_domain, api_key=api_key)

    def get_routes(self, limit=100, skip=0):
        """
        fetches the list of routes
        :param limit: maximum number of records to return
        :param skip: number of records to skip
        """
        parameters = {"limit": limit,
                      "skip": skip}

        return self.get("routes", **parameters)

    def get_route(self, route_id):
        """
        returns a single route object based on its ID
        :param route_id: id of the route
        """
        return self.get("routes/" + route_id)

    def create_route(self, priority, description, expression, action):
        """
        creates a new route
        :param priority: Integer: smaller number indicates higher priority. Higher priority routes are handled first. Defaults to 0
        :param description: an arbitrary string
        :param expression: a filter expression like match_recipient('.*@gmail.com')
        :param action: route action
        """
        parameters = {"priority": priority,
                      "description": description,
                      "expression": expression,
                      "action": action}
        return self.post("routes", **parameters)

    def update_route(self, route_id, **kwargs):
        """
        updates a given route by ID
        :param route_id: id of the route
        :param kwargs: 
            priority: Integer: smaller number indicates higher priority. Higher priority routes are handled first. Defaults to 0
            description: an arbitrary string
            expression: a filter expression like match_recipient('.*@gmail.com')
            action: route action
        """
        return self.put("routes/" + route_id, **kwargs)

    def remove_route(self, route_id):
        """
        deletes a route based on the id
        :param route_id: id of the route
        """
        return self.delete("routes/" + route_id)
