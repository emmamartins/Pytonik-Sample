# Author : BetaCodings
# Author : info@betacodings.com
# Maintainer By: Emmanuel Martins
# Maintainer Email: emmamartinscm@gmail.com
# Created by BetaCodings on 1/18/20.

from pytonik import Web

m = Web.App()

def index():


    data = {

        'title' : 'Users Controller',
        'text': 'Welcome to My pytonik Users Page',

    }

    m.views('users', data)

def login(Request):

    username , password = "", ""

    if Request.method == "POST":
        username = Request.post('username')
        password = Request.post('password')


    data = {

        'title': 'My Pytonik Login Page',
        'usertext': 'User Login',
        'username': username,
        'password': password

    }

    m.views('login', data)

def register(Request):

    from pytonik.Functions.validation import validation

    validate = validation()
    msg = ""
    if Request.method == "POST":
        firstname = Request.post('firstname')
        lastname = Request.post('lastname')
        email = Request.post('email')
        phonenumber = Request.post('phonenumber')
        username = Request.post('username')
        password = Request.post('password')

        if firstname == "":
            msg = "Enter First Name"
        elif lastname == "":
            msg = "Enter Last Name"
        elif email == "":
            msg = "Enter Email Address"
        elif validate.email(email) is False:
            msg = "Invalid Email Address"
        elif phonenumber == "":
            msg = "Enter Phone Number"
        elif validate.phone(phonenumber) is False:
            msg = "Invalid Phone Number"
        elif username == "":
            msg = "Enter Username"
        elif password == "":
            msg = "Enter Password"
        else:
            msg = "Registration is successful"

    data = {

        'title': 'My Pytonik Register Page',
        'registertext': 'User Registration',
        'msg': msg,
        'url': 'url',
    }
    m.views('register', data)