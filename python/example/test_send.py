#!/usr/bin/python
#-*-coding: utf8-*-

from mailgun.data.msg_data import MsgData
from mailgun.message import Message

if __name__ == "__main__":
    from_email = ("fatelei", "foo@gmail.com")
    to = [{"name": "test", "email": "bar@qq.com"}]
    subject = "test"
    html = "<h1>Hello World</h1>"
    msgdata = MsgData(from_email, to, subject, html=html)
    data, files = msgdata.to_json()

    message = Message("domain", "api-ket")

    print data, files

    kwargs = {}

    if files:
        kwargs["files"] = files

    if data:
        kwargs["data"] = data

    print message.send_messages(**kwargs)
