#-*-coding: utf8-*-

"""
mailgun domains api
"""

from .client import MailgunClient


class APIDomains(MailgunClient):

    """The domain api
    """

    def __init__(self, api_url=None, api_key=None):
        """Init the class
        """
        super(APIDomains, self).__init__(
            api_url=api_url, api_domain=None, api_key=api_key)

    def get_domains(self, limit=100, skip=0):
        """Return a list of domains.

        Args:
            limit: The maximum number of records to return
            skip: The number of records to skip
        """
        parameters = {"limit": limit, "skip": skip}
        return self.get("domains", **parameters)

    def get_domain(self, domain):
        """Returns a single domain, including credentials and DNS records.

        Args:
            domain: The name of domain
        """
        return self.get("domains/" + domain)

    def create_new_domain(self, name, smtp_password, wildcard):
        """Create new domain

        Args:
            name: The name of the domain
            smtp_password: The password for SMTP authentication
            wildcard: True or false Determines whether the domain will accept email for sub-domains.
        """
        parameters = {"name": name,
                      "smtp_password": smtp_password,
                      "wildcard": wildcard}
        return self.post("domains", **parameters)

    def remove_domain(self, domain):
        """Remove domain

        Args:
            domain: The name of the domain
        """
        return self.delete("domains/" + domain)

    def get_domain_credentials(self, domain, limit=100, skip=0):
        """Returns a list of SMTP credentials for the defined domain

        Args:
            domain: The name of the domain
            limit: The maximum number of records to return
            skip: The number of records to skip
        """
        parameters = {"limit": limit, "skip": skip}
        return self.get("domains/" + domain, **parameters)

    def create_domain_credentials(self, domain, login, password):
        """Creates a new set of SMTP credentials for the defined domain.

        Args:
            domain: The name of the domain
            login: The user name, for example bob.bar
            password: A password for the SMTP credentials. (Length Min 5, Max 32
        """
        if len(password) < 5 or len(password) > 32:
            raise Exception("password's length must be between 5 and 22")
        parameters = {"login": login,
                      "password": password}
        return self.post("domains/" + domain + "/credentials", **parameters)

    def remove_domain_credentials(self, domain, login):
        """Deletes the defined SMTP credentials

        Args:
            domain: The name of the domain
            login: The user name
        """
        return self.delete("domains/" + domain + "/credentials/" + login)
