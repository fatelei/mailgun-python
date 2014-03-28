#-*-coding: utf8-*-

"""
mailgun mailing lists api
"""

from .client import MailGunClient


class APIMailingLists(MailGunClient):

    def __init__(self, api_url=None, api_key=None):
        super(APIMailingLists, self).__init__(
            api_url=api_url, api_key=api_key)

    def get_mailing_lists(self, address=None, limit=100, skip=0):
        """
        returns a list of mailing lists under your account
        @param address: find a mailing list by it’s address (optional)
        @param limit: maximum number of records to return
        @param skip: number of records to skip
        """
        parameters = {"limit": limit, "skip": skip}
        if address is not None:
            parameters["address"] = address

        return self.get("lists", **parameters)

    def get_mailing_list(self, address):
        """
        returns a single mailing list by a given address
        @param address: email address
        """
        return self.get("lists/" + address)

    def add_to_mailing_lists(self, address, access_level="readonly", name=None, description=None):
        """
        creates a new mailing list
        @param address: a valid email address for the mailing list
        @param name: mailing list name (optional)
        @param description: a description (optional)
        @param access_level: list access level, one of: readonly (default), members, everyone
        """
        parameters = {"address": address, "access_level": access_level}

        if name is not None:
            parameters["name"] = name

        if description is not None:
            parameters["description"] = description

        return self.post("lists", **parameters)

    def update_mailing_list(self, old_address, new_address=None, access_level="readonly", name=None, description=None):
        """
        updates a new mailing list
        @param address: a valid email address for the mailing list
        @param name: mailing list name (optional)
        @param description: a description (optional)
        @param access_level: list access level, one of: readonly (default), members, everyone
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
        """
        deletes a mailing list
        @param address: eamil address
        """
        return self.delete("lists/" + address)

    def get_members_from_mailing_list(self, address, subscribed, limit=100, skip=0):
        """
        fetches the list of mailing list members
        @param address: email address
        @param subscribed: yes to list subscribed, no for unsubscribed, list all if not set
        @param limit: maximum number of records to return
        @param skip: number of records to skip
        """
        parameters = {"subscribed": subscribed, "limit": limit, "skip": skip}
        return self.get("lists/" + address + "/members", **parameters)

    def get_member_from_mailing_list(self, address, member_address):
        """
        retrieves a mailing list member
        @param address: email address
        @param member_address: member's email address
        """
        return self.get("lists/" + address + "/members/" + member_address)

    def add_member_to_mailing_list(self, address, memeber_address, name=None, vars=None, subscribed="yes", upset="yes"):
        """
        adds a member to the mailing list
        @param address: email address of the mailing list
        @param member_address: valid email address specification
        @param name: optinal member name
        @param vars: JSON-encoded dictionary string with arbitrary parameters, e.g. {"gender":"female","age":27}
        @param subscribed: yes to add as subscribed (default), no as unsubscribed
        @param upset: yes to update member if present, no to raise error in case of a duplicate member (default)
        """
        parameters = {"address": memeber_address,
                      "subscribed": subscribed, "upset": upset}

        if name is not None:
            parameters["name"] = name

        if vars is not None:
            parameters["vars"] = vars

        return self.post("lists/" + address + "/members", **parameters)

    def update_member_in_mailing_list(self, address, member_address, new_member_address=None, name=None, vars=None, subscribed="yes"):
        """
        updates a mailing list member with given properties. Won’t touch the property if it’s not passed in
        @param address: email address of the mailing list
        @param member_address: old member address
        @param new_member_address: new member address (optional)
        @param name: optional member name
        @param vars: JSON-encoded dictionary string with arbitrary parameters, e.g. {"gender":"female","age":27}
        @param subscribed: yes to add as subscribed (default), no as unsubscribed
        """
        parameters = {"subscribed": subscribed}

        if new_member_address is not None:
            parameters["address"] = new_member_address

        if name is not None:
            parameters["name"] = name

        if vars is not None:
            parameters["vars"] = vars

        return self.put("lists/" + address + "/members/" + member_address, **parameters)

    def remove_member_from_mailing_list(self, address, member_address):
        """
        delete a mailing list member
        @param address: email address of the mailing list
        @param member_address: email address of tha mailing list member
        """
        return self.delete("lists/" + address + "/members/" + member_address)
