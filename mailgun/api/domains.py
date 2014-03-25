#-*-coding: utf8-*-

"""
mailgun domains api
"""

from .client import MailGunClient


class APIDomains(MailGunClient):

    def __init__(self, api_url=None, api_key=None):
        super(APIDomains, self).__init__(
            api_url=api_url, api_domain=None, api_key=api_key)

    def get_domains(self, limit=100, skip=0):
        """
        return a list of domains
        :param limit: maximum number of records to return
        :param skip: number of records to skip
        """
        parameters = {"limit": limit, "skip": skip}
        return self.get("domains", **parameters)

    def get_domain(self, domain):
        return self.get("domains/" + domain)

    def create_new_domain(self, name, smtp_password, wildcard):
        """
        create new domain
        :param name: name of the domain
        :param smtp_password: password for SMTP authentication
        :param wildcard: true or false Determines whether the domain will accept email for sub-domains.
        """
        parameters = {"name": name,
                      "smtp_password": smtp_password,
                      "wildcard": wildcard}
        return self.post("domains", **parameters)

    def remove_domain(self, domain):
        """
        remove domain
        :param domain: name of the domain
        """
        return self.delete("domains/" + domain)

    def get_domain_credentials(self, domain, limit=100, skip=0):
        """
        returns a list of SMTP credentials for the defined domain
        :param domain: name of the domain
        :param limit: maximum number of records to return
        :param skip: number of records to skip
        """
        parameters = {"limit": limit, "skip": skip}
        return self.get("domains/" + domain, **parameters)

    def create_domain_credentials(self, domain, login, password):
        """
        creates a new set of SMTP credentials for the defined domain.
        :param domain: name of the domain
        :param login: the user name, for example bob.bar
        :param password: a password for the SMTP credentials. (Length Min 5, Max 32
        """
        if len(password) < 5 or len(password) > 32:
            raise Exception("password's length must be between 5 and 22")
        parameters = {"login": login,
                      "password": password}
        return self.post("domains/" + domain + "/credentials", **parameters)

    def remove_domain_credentials(self, domain, login):
        """
        deletes the defined SMTP credentials
        :param domain: name of the domain
        :param login: the user name
        """
        return self.delete("domains/" + domain + "/credentials/" + login)
