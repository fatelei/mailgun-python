#-*-coding: utf8-*-

"""
message data for api messages

TODO:
    add_attachment
    add_inline
    add_mime_message
"""

from lepl.apps import rfc3696
from mailgun.utils import date_format


class Message(object):

    def __init__(self):
        self.data = {"to": []}
        self.email_validator = rfc3696.Email()

    def add_from(self, from_addr):
        """
        add sender
        :param from_addr: email address of sender
        """
        if not self.email_validator(from_addr):
            raise Exception("email format is invalid")

        self.data["from"] = from_addr

    def add_to(self, to_name, to_addr):
        """
        add recipients
        :param to: email address of recipients
        """
        if not self.email_validator(to_addr):
            raise Exception("email format is invalid")

        recipient = "{0} {1}".format(to_name, to_addr)
        self.data["to"].append(recipient)

    def add_cc(self, cc):
        """
        add cc
        :param cc: email address of cc
        """
        if not self.email_validator(cc):
            raise Exception("email format is invalid")

        self.data["cc"] = cc

    def add_bcc(self, bcc):
        """
        add bcc
        :param bcc: email address of bcc
        """
        if not self.email_validator(bcc):
            raise Exception("email format is invalid")

        self.data["bcc"] = bcc

    def add_subject(self, subject):
        """
        add subject
        :param subject: email subject
        """
        self.data["subject"] = subject

    def add_text(self, text):
        """
        add text
        :param text: text content
        """
        self.data["text"] = text

    def add_html(self, html):
        """
        add html
        :param html: html content
        """
        self.data["html"] = html

    def add_attachment(self, attachment):
        """
        add attachment
        :param attachment: file attachment
        """
        pass

    def add_inline(self, inline):
        """
        add inline
        :param inline: inline data
        """
        pass

    def add_tag(self, tag):
        """
        add tag
        :param tag: track tag
        """
        self.data["o:tag"] = tag

    def add_campaign(self, campaign):
        """
        add campaign
        :param campaign: track campaign
        """
        self.data["o:campaign"] = campaign

    def add_dkim(self, dkim):
        """
        enable / disable dkim
        :param dkim: yes or no
        """
        if dkim not in ["yes", "no"]:
            raise Exception("dkim's value must be 'yes' or 'no'")
        self.data["o:dkim"] = dkim

    def add_delivery_time(self, date):
        """
        add schedule delivery time
        :param date: datetime
        """
        date = date_format(date)
        self.data["o:deliverytime"] = date

    def add_testmode(self, testmode):
        """
        enable / disable testmmode
        :param testmode: yes or no
        """
        if testmode not in ["yes", "no"]:
            raise Exception("testmode's value must be 'yes' or 'no'")
        self.data["o:testmode"] = testmode

    def add_tracking(self, tracking):
        """
        enable / disable tracking
        :param tracking: yes or no
        """
        if tracking not in ["yes", "no"]:
            raise Exception("tracking's value must be 'yes' or 'no'")
        self.data["o:tracking"] = tracking

    def add_tracking_clicks(self, tracking_clicks):
        """
        enable / disable tracking clicks
        :param tracking_clicks: yes, no or htmlonly
        """
        if tracking_clicks not in ["yes", "no", "htmlonly"]:
            raise Exception(
                "trackinng_clicks's value must be yes, no or htmlonly")
        self.data["o:tracking-clicks"] = tracking_clicks

    def add_tracking_opens(self, tracking_opens):
        """
        enable / disable tracking opens
        :param tracking_opens: yes or no
        """
        if tracking_opens not in ["yes", "no"]:
            raise Exception("tracking_opens's value must be yes or no")
        self.data["o:tracking-opens"] = tracking_opens

    def add_custom_header(self, header, value):
        """
        add custom MIME header
        :param header: header name
        :param value: header value
        """
        self.data["h:" + header] = value

    def add_custom_variables(self, key, value):
        """
        add custom variables
        :param key: variable key
        :param value: variable value
        """
        self.data["v:" + key] = value

    def add_mime_message(self, message):
        """
        add mime message
        :param message: mime message
        """
        pass

    def generate(self):
        """
        generate parameters
        """
        if len(self.data["to"]) > 1:
            self.data["to"] = ",".join(self.data["to"])

        return self.data
