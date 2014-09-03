#-*-coding: utf8-*-

"""
Message data for api messages

TODO:
    add_attachment
    add_inline
    add_mime_message
"""

from lepl.apps import rfc3696


class Message(object):

    """The meta info of message

    Attributes:
        data: A dict contains the detail info of message
        email_validator: An email validator
    """

    def __init__(self):
        """Init the class
        """
        self.data = {"to": []}
        self.email_validator = rfc3696.Email()

    def add_from(self, from_addr, from_name=None):
        """Add sender

        Args:
            from_addr: An email address of sender
        """
        if not self.email_validator(from_addr):
            raise Exception("email format is invalid")

        if from_name is not None:
            from_ = "%s <%s>" % (from_name, from_addr)
        else:
            from_ = "%s" % from_addr
        self.data["from"] = from_

    def add_to(self, to_addr, to_name=None):
        """Add recipients

        Args:
            to: The email address of recipients
        """
        if not self.email_validator(to_addr):
            raise Exception("email format is invalid")

        if to_name is not None:
            recipient = "%s <%s>" % (to_name, to_addr)
        else:
            recipient = "%s" % to_addr
        self.data["to"].append(recipient)

    def add_cc(self, cc):
        """Add cc

        Args:
            cc: The email address of cc
        """
        if not self.email_validator(cc):
            raise Exception("email format is invalid")

        self.data["cc"] = cc

    def add_bcc(self, bcc):
        """Add bcc

        Args:
            bcc: The email address of bcc
        """
        if not self.email_validator(bcc):
            raise Exception("email format is invalid")

        self.data["bcc"] = bcc

    def add_subject(self, subject):
        """Add subject

        Args:
            subject: The email subject
        """
        self.data["subject"] = subject

    def add_text(self, text):
        """Add text

        Args:
            text: The text content
        """
        self.data["text"] = text

    def add_html(self, html):
        """Add html

        Args:
            html: The html content
        """
        self.data["html"] = html

    def add_attachment(self, attachment):
        """Add attachment

        Args:
            attachment: File attachment
        """
        pass

    def add_inline(self, inline):
        """Add inline

        Args
            inline: The inline data
        """
        pass

    def add_tag(self, tag):
        """Add tag

        Args:
            tag: A track tag
        """
        self.data["o:tag"] = tag

    def add_campaign(self, campaign):
        """Add campaign

        Args:
            campaign: A track campaign
        """
        self.data["o:campaign"] = campaign

    def add_dkim(self, dkim):
        """Enable / disable dkim

        Args:
            dkim: Yes or no
        """
        if dkim not in ["yes", "no"]:
            raise Exception("dkim's value must be 'yes' or 'no'")
        self.data["o:dkim"] = dkim

    def add_delivery_time(self, date):
        """Add schedule delivery time

        Args:
            date: A datetime
        """
        self.data["o:deliverytime"] = date

    def add_testmode(self, testmode):
        """Enable / disable testmmode

        Args:
            testmode: Yes or no
        """
        if testmode not in ["yes", "no"]:
            raise Exception("testmode's value must be 'yes' or 'no'")
        self.data["o:testmode"] = testmode

    def add_tracking(self, tracking):
        """Enable / disable tracking

        Args:
            tracking: Yes or no
        """
        if tracking not in ["yes", "no"]:
            raise Exception("tracking's value must be 'yes' or 'no'")
        self.data["o:tracking"] = tracking

    def add_tracking_clicks(self, tracking_clicks):
        """Enable / disable tracking clicks

        Args:
            tracking_clicks: Yes, no or htmlonly
        """
        if tracking_clicks not in ["yes", "no", "htmlonly"]:
            raise Exception(
                "trackinng_clicks's value must be yes, no or htmlonly")
        self.data["o:tracking-clicks"] = tracking_clicks

    def add_tracking_opens(self, tracking_opens):
        """Enable / disable tracking opens

        Args:
            tracking_opens: Yes or no
        """
        if tracking_opens not in ["yes", "no"]:
            raise Exception("tracking_opens's value must be yes or no")
        self.data["o:tracking-opens"] = tracking_opens

    def add_custom_header(self, header, value):
        """Add custom MIME header

        Args:
            header: A header name
            value: A header value
        """
        self.data["h:" + header] = value

    def add_custom_variables(self, key, value):
        """Add custom variables

        Args:
            key: A variable key
            value: A variable value
        """
        self.data["v:" + key] = value

    def add_mime_message(self, message):
        """Add mime message

        Args:
            message: A mime message
        """
        pass

    def generate(self):
        """Generate parameters
        """
        self.data["to"] = ",".join(self.data["to"])

        return self.data
