#-*-coding: utf8-*-

"""
mailgun mailing lists api
"""

from .client import MailgunClient


class APIMailingLists(MailgunClient):

    """The mailing list api
    """

    def __init__(self, api_url=None, api_key=None):
        """Init the class
        """
        super(APIMailingLists, self).__init__(
            api_url=api_url, api_key=api_key)

    def get_mailing_lists(self, address=None, limit=100, skip=0):
        """Returns a list of mailing lists under your account

        Args:
            address: Find a mailing list by it’s address (optional)
            limit: The maximum number of records to return
            skip: The number of records to skip
        """
        parameters = {"limit": limit, "skip": skip}
        if address is not None:
            parameters["address"] = address

        return self.get("lists", **parameters)

    def get_mailing_list(self, address):
        """Returns a single mailing list by a given address

        Args:
            address: The email address
        """
        return self.get("lists/" + address)

    def add_to_mailing_lists(self,
                             address,
                             access_level="readonly",
                             name=None,
                             description=None):
        """Creates a new mailing list

        Args:
            address: A valid email address for the mailing list
            name: The mailing list name (optional)
            description: A description (optional)
            access_level: The list access level, one of: readonly (default), members, everyone
        """
        parameters = {"address": address, "access_level": access_level}

        if name is not None:
            parameters["name"] = name

        if description is not None:
            parameters["description"] = description

        return self.post("lists", **parameters)

    def update_mailing_list(self,
                            old_address,
                            new_address=None,
                            access_level="readonly",
                            name=None,
                            description=None):
        """Updates a new mailing list

        Args:
            address: A valid email address for the mailing list
            name: The mailing list name (optional)
            description: A description (optional)
            access_level: The list access level, one of: readonly (default), members, everyone
        """
        parameters = {"access_level": access_level}

        if new_address is not None:
            parameters["address"] = new_address

        if name is not None:
            parameters["name"] = name

        if description is not None:
            parameters["description"] = description

        return self.put("lists/" + old_address, **parameters)

    def remove_from_mailing_lists(self, address):
        """Deletes a mailing list

        Args:
            address: The eamil address
        """
        return self.delete("lists/" + address)

    def get_members_from_mailing_list(self,
                                      address,
                                      subscribed,
                                      limit=100,
                                      skip=0):
        """Fetches the list of mailing list members

        Args:
            address: The email address
            subscribed: Yes to list subscribed, no for unsubscribed, list all if not set
            limit: The maximum number of records to return
            skip: The number of records to skip
        """
        parameters = {"subscribed": subscribed, "limit": limit, "skip": skip}
        return self.get("lists/" + address + "/members", **parameters)

    def get_member_from_mailing_list(self, address, member_address):
        """Retrieves a mailing list member

        Args:
            address: The email address
            member_address: The member's email address
        """
        return self.get("lists/" + address + "/members/" + member_address)

    def add_member_to_mailing_list(self,
                                   address,
                                   memeber_address,
                                   name=None,
                                   vars=None,
                                   subscribed="yes",
                                   upset="yes"):
        """Adds a member to the mailing list

        Args:
            address: The email address of the mailing list
            member_address: A valid email address specification
            name: A optinal member name
            vars: JSON-encoded dictionary string with arbitrary parameters, e.g. {"gender":"female","age":27}
            subscribed: Yes to add as subscribed (default), no as unsubscribed
            upset: Yes to update member if present, no to raise error in case of a duplicate member (default)
        """
        parameters = {"address": memeber_address,
                      "subscribed": subscribed, "upset": upset}

        if name is not None:
            parameters["name"] = name

        if vars is not None:
            parameters["vars"] = vars

        return self.post("lists/" + address + "/members", **parameters)

    def update_member_in_mailing_list(self,
                                      address,
                                      member_address,
                                      new_member_address=None,
                                      name=None,
                                      vars=None,
                                      subscribed="yes"):
        """Updates a mailing list member with given properties.
        Won’t touch the property if it’s not passed in

        Args:
            address: The email address of the mailing list
            member_address: An old member address
            new_member_address: A new member address (optional)
            name: An optional member name
            vars: JSON-encoded dictionary string with arbitrary parameters, e.g. {"gender":"female","age":27}
            subscribed: Yes to add as subscribed (default), no as unsubscribed
        """
        parameters = {"subscribed": subscribed}

        if new_member_address is not None:
            parameters["address"] = new_member_address

        if name is not None:
            parameters["name"] = name

        if vars is not None:
            parameters["vars"] = vars

        url = "lists/" + address + "/members/" + member_address
        return self.put(url, **parameters)

    def remove_member_from_mailing_list(self, address, member_address):
        """Delete a mailing list member

        Args:
            address: An email address of the mailing list
            member_address: An email address of tha mailing list member
        """
        return self.delete("lists/" + address + "/members/" + member_address)
