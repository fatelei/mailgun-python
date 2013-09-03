#!/usr/bin/python
#-*-coding: utf8-*-

import logging

from base import Base


class MsgData(Base):

    """
    the message send to mailgun
    """

    def __init__(self, from_email, to, subject, text=None, html=None):
        """
        args:
            from_email: the sender's email address, example (displayname, email address)
            to: the receivers' info, example [{name: xx, email: xx}]
            subject: the theme of email
            text: pure text content
            html: html content
        """
        self.validate_data_type(from_email, tuple)

        sender_name, sender_email = from_email

        try:
            self.validate_email(sender_email)
        except Exception as e:
            raise ValueError(u"%s is not a valid address" % sender_email)

        self.from_email = "{0} <{1}>".format(sender_name, sender_email)
        self.to = self.__add_receivers(to)

        self.cc = None
        self.bcc = None
        self.subject = subject
        self.text = text
        self.html = html
        self.attachment = {"attachment": ""}
        self.inline = {"inline": []}
        self.tag = []
        self.campaign = {}

    def __add_receivers(self, receivers):
        """
        add receivers

        args:
            recerivers: the receivers' info, example [{name: xx, email: xx}]
        """
        self.validate_data_type(receivers, list)

        to = []
        for receiver in receivers:
            try:
                self.validate_email(receiver["email"])
                to.append(
                    "{0} <{1}>".format(receiver["name"], receiver["email"]))
            except Exception as e:
                loggging.warning(e)
        if len(to) == 0:
            raise Exception(u"receivers can't be empty!")
        return to

    def add_cc(self, cc):
        """
        add cc

        args:
            cc: the receivers' info, example [{name: xx, email: xx}]
        """
        if not cc:
            self.cc = self.__add_receivers(cc)

    def add_bcc(self, bcc):
        """
        add bcc

        args:
            bcc: the receivers' info, example [{name: xx, email: xx}]
        """
        if not bcc:
            self.bcc = self.__add_receivers(bcc)

    def add_attachment(self, attachment):
        """
        add attachment

        """
        if attachment:
            self.attachment["attachment"] = attachment

    def add_inline(self, inline):
        """
        add inline attachment
        """
        if inline:
            self.validate_data_type(inline, file)
            self.inline["inline"].append(inline)

    def add_tag(self, tag):
        """
        add tag
        """
        if tag:
            self.tag.append({"o:tag": tag})

    def add_campaign(self, campaign):
        """
        add campaign
        """
        self.campaign["o:campaign"] = campaign

    def to_request_data(self):
        """
        convert request data to json data
        """
        data = {}
        files = {}

        data["from"] = self.from_email
        data["to"] = self.to

        if self.text:
            data["text"] = self.text

        if self.html:
            data["html"] = self.html

        if self.cc:
            data["cc"] = self.cc

        if self.bcc:
            data["bcc"] = self.bcc

        if self.tag:
            data.update(self.tag)

        if self.campaign:
            data.update(self.campaign)

        if self.attachment["attachment"]:
            files["attachment"] = self.attachment["attachment"]

        if self.inline["inline"]:
            files["inline"] = self.inline["inline"]

        return data, files
