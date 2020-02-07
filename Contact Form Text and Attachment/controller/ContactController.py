# Author : BetaCodings
# Author : info@betacodings.com
# Maintainer By: Emmanuel Martins
# Maintainer Email: emmamartinscm@gmail.com
# Created by BetaCodings on 1/18/20.

from pytonik import Web
from pytonik.Core.SMTP import SMTP
from pytonik.Functions.validation import validation

m = Web.App()
mail = SMTP()
validate = validation()

def index(Request):
    fullname, email, subject, message = "", "", "", ""

    msg = ""
    if Request.method == "POST":
        fullname = Request.post('fullname')
        email = Request.post('email')
        subject = Request.post('subject')
        message = Request.post('message')

        if fullname == "":
            msg = "Enter Fullname"
        elif email == "":
            msg = "Enter Email Address"
        elif validate.email(email) is False:
            msg = "Invalid Email Address"
        elif subject == "":
            msg = "Enter Subject"

        elif message == "":
            msg = "Enter Message"

        else:
            content = """
            Full Name: {name} <br/>
            Message: {message}
            """.format(name = fullname, message = message)

            fromemail = "email@email.com"

            send = mail.send(fromemail, email, subject, content, 'html')

            if send is True:
                msg = "Email Sent Successfully "
            else:
                msg = "Unable to Send Email"

    data = {

        'title' : 'Contact Controller',
        'text': 'Welcome to My pytonik Contact Page',
        'msg' : msg
    }

    m.views('sent', data)

def attach(Request):
    fullname, email, subject, message = "", "", "", ""

    msg = ""
    if Request.method == "POST":
        fullname = Request.post('fullname')
        email = Request.post('email')
        subject = Request.post('subject')
        message = Request.post('message')
        file = Request.file('attached')

        if fullname == "":
            msg = "Enter Fullname"
        elif email == "":
            msg = "Enter Email Address"
        elif validate.email(email) is False:
            msg = "Invalid Email Address"
        elif subject == "":
            msg = "Enter Subject"

        elif message == "":
            msg = "Enter Message"

        else:
            content = """
            Full Name: {name} <br/>
            Message: {message}
            """.format(name = fullname, message = message)

            fromemail = "email@email.com"

            send = mail.attach(file).send(fromemail, email, subject, content, 'html')

            if send is True:
                msg = "Email Sent Successfully "
            else:
                msg = "Unable to Send Email"

    data = {

        'title' : 'Contact Controller',
        'text': 'Welcome to My pytonik Contact Attachment Page',
        'msg' : msg
    }

    m.views('attach', data)
